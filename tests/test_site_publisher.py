import json
import tempfile
import unittest
from pathlib import Path

from scripts.site import PublicationError, build_site, validate_bundle


class ParentGuidePublisherTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "config").mkdir()
        (self.root / "templates").mkdir()
        (self.root / "content" / "production" / "2026-08-10-example" / "media").mkdir(parents=True)
        (self.root / "config" / "site.json").write_text(
            json.dumps(
                {
                    "site_name": "Old Wisdom // Retold",
                    "base_url": "https://oldwisdomretold.com",
                    "author": "Eric Han",
                    "language": "en-NZ",
                    "parent_hub_path": "parents/index.html",
                    "parent_growth_brevo_form_action": "https://example.com/subscribe",
                }
            ),
            encoding="utf-8",
        )
        (self.root / "templates" / "parent-guide.html").write_text(
            "<!-- AUDIENCE: PARENT -->\n{{article_title}}|{{seo_title}}|{{seo_description}}|{{canonical}}|{{social_image}}|{{social_image_alt}}|{{article_schema}}|{{journey_stage}}|{{summary}}|{{author}}|{{published_display}}|{{reading_time}}|{{hero}}|{{body}}|{{release_move}}|{{next_step}}|{{parent_growth_signup}}",
            encoding="utf-8",
        )
        (self.root / "templates" / "parent-hub.html").write_text(
            "{{canonical}}|{{collection_schema}}|{{journey_map}}|{{guide_sections}}|{{parent_growth_signup}}", encoding="utf-8"
        )
        (self.root / "sitemap.xml").write_text(
            "<urlset>\n<!-- PARENT-HUB:START -->\n<!-- PARENT-HUB:END -->\n</urlset>", encoding="utf-8"
        )
        (self.root / "llms.txt").write_text(
            "# Site\n<!-- PARENT-HUB:START -->\n<!-- PARENT-HUB:END -->", encoding="utf-8"
        )
        self.bundle = self.root / "content" / "production" / "2026-08-10-example"
        (self.bundle / "ARTICLE.md").write_text(
            "<!-- AUDIENCE: PARENT -->\n\n# Example Guide\n\n## What to notice\n\nA useful paragraph for parents.", encoding="utf-8"
        )
        (self.bundle / "SOURCES.md").write_text("# Sources\n\n- https://example.com", encoding="utf-8")
        pins = []
        for number in range(1, 6):
            pins.append(
                f"## Pin {number}\n\n- Title: Example {number}\n- Description: Useful guide https://oldwisdomretold.com/quiz.html?utm_source=pinterest&utm_medium=organic&utm_campaign=example&utm_content=example-{number}"
            )
        (self.bundle / "PINTEREST.md").write_text("\n\n".join(pins), encoding="utf-8")
        for name in ("hero.webp", "hero-480.webp", "hero-800.webp", "og.webp"):
            (self.bundle / "media" / name).write_bytes(b"image")

    def tearDown(self):
        self.temp_dir.cleanup()

    def manifest(self):
        return {
            "schema_version": 2,
            "status": "published",
            "audience": "parent",
            "slug": "example-guide",
            "title": "Example Guide",
            "summary": "A useful guide for testing the Parent Growth publishing boundary.",
            "published": "2026-08-10",
            "journey_stage": "GUIDE",
            "supports_stages": ["SEE", "UNDERSTAND", "REFLECT", "RELEASE"],
            "teen_outcomes": ["capability", "ownership"],
            "release_move": "Let the teenager decide which small practice feels useful and what they will try next.",
            "qa_score": 18,
            "territory": "connection",
            "test_angle": "LONG_TERM_CAPABILITY",
            "core_belief_shift": {
                "from": "A teen needs to feel confident before attempting a social move.",
                "to": "A teen builds confidence by choosing and repeating one manageable social move.",
            },
            "book_relevance": {
                "status": "none",
                "reason": "The most useful next step is the guide's practice, not a product recommendation.",
            },
            "hero": {
                "source": "media/hero.webp",
                "alt": "A parent listening to a teenager",
                "width": 1200,
                "height": 675,
                "variants": [
                    {"source": "media/hero-480.webp", "width": 480},
                    {"source": "media/hero-800.webp", "width": 800},
                ],
            },
            "social_image": {"source": "media/og.webp", "alt": "A parent listening to a teenager"},
            "pinterest_campaign": {"campaign": "example", "content": "example-guide"},
            "next_step": {"kind": "none"},
        }

    def write_manifest(self, data):
        path = self.bundle / "PUBLISH.json"
        path.write_text(json.dumps(data), encoding="utf-8")
        return path

    def test_build_generates_parent_hub_article_and_catalogue_entries(self):
        self.write_manifest(self.manifest())

        changed = build_site(self.root)

        article = self.root / "articles" / "example-guide.html"
        self.assertIn(article, changed)
        self.assertTrue(article.exists())
        article_content = article.read_text(encoding="utf-8")
        self.assertEqual(article_content.count("<!-- AUDIENCE: PARENT -->"), 1)
        self.assertNotIn("&lt;!-- AUDIENCE: PARENT --&gt;", article_content)
        self.assertIn("Example Guide", article_content)
        self.assertTrue((self.root / "parents" / "index.html").exists())
        self.assertIn("example-guide", (self.root / "sitemap.xml").read_text(encoding="utf-8"))
        self.assertIn("Parent Hub", (self.root / "llms.txt").read_text(encoding="utf-8"))
        self.assertTrue((self.root / "assets" / "parent-hub" / "example-guide" / "hero.webp").exists())
        self.assertEqual(build_site(self.root, check_only=True), [])

    def test_playbook_next_step_requires_explicit_relevance(self):
        data = self.manifest()
        data["next_step"] = {"kind": "playbook", "id": "war"}
        path = self.write_manifest(data)

        with self.assertRaisesRegex(PublicationError, "relevance reason"):
            validate_bundle(self.root, path)

    def test_v4_governance_gates_reject_weak_or_incomplete_metadata(self):
        cases = [
            ("qa_score", 15, "qa_score"),
            ("territory", "parenting", "territory"),
            ("test_angle", "GUIDE", "test_angle"),
            ("core_belief_shift", {"from": "Too short", "to": "Also too short"}, "core_belief_shift"),
            ("book_relevance", {"status": "relevant", "reason": "A Playbook might help with the topic."}, "recognised Playbook id"),
        ]
        for field, value, message in cases:
            with self.subTest(field=field):
                data = self.manifest()
                data[field] = value
                path = self.write_manifest(data)
                with self.assertRaisesRegex(PublicationError, message):
                    validate_bundle(self.root, path)

    def test_playbook_next_step_must_match_declared_book_relevance(self):
        data = self.manifest()
        data["book_relevance"] = {
            "status": "relevant",
            "id": "social",
            "reason": "The Social Playbook develops the same conversation skill in more depth.",
        }
        data["next_step"] = {"kind": "playbook", "id": "war", "reason": "A mismatched CTA."}
        path = self.write_manifest(data)

        with self.assertRaisesRegex(PublicationError, "must match"):
            validate_bundle(self.root, path)

    def test_pinterest_campaign_requires_every_pin_to_keep_utm_attribution(self):
        self.write_manifest(self.manifest())
        campaign = self.bundle / "PINTEREST.md"
        campaign.write_text("## Pin 1\n\n- Title: Missing attribution\n- Description: No link", encoding="utf-8")

        with self.assertRaisesRegex(PublicationError, "expected five titled pins"):
            validate_bundle(self.root, self.bundle / "PUBLISH.json")

    def test_build_is_deterministic_and_missing_managed_marker_fails_closed(self):
        self.write_manifest(self.manifest())
        build_site(self.root)
        first_sitemap = (self.root / "sitemap.xml").read_bytes()
        self.assertEqual(build_site(self.root, check_only=True), [])
        self.assertEqual(first_sitemap, (self.root / "sitemap.xml").read_bytes())

        (self.root / "llms.txt").write_text("# Site without generated region", encoding="utf-8")
        with self.assertRaisesRegex(PublicationError, "missing or duplicate managed region"):
            build_site(self.root)


if __name__ == "__main__":
    unittest.main()
