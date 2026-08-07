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
                }
            ),
            encoding="utf-8",
        )
        (self.root / "templates" / "parent-guide.html").write_text(
            "{{title}}|{{description}}|{{canonical}}|{{social_image}}|{{social_image_alt}}|{{article_schema}}|{{journey_stage}}|{{summary}}|{{author}}|{{published_display}}|{{reading_time}}|{{hero}}|{{body}}|{{release_move}}|{{next_step}}",
            encoding="utf-8",
        )
        (self.root / "templates" / "parent-hub.html").write_text(
            "{{canonical}}|{{collection_schema}}|{{journey_map}}|{{guide_sections}}", encoding="utf-8"
        )
        (self.root / "sitemap.xml").write_text(
            "<urlset>\n<!-- PARENT-HUB:START -->\n<!-- PARENT-HUB:END -->\n</urlset>", encoding="utf-8"
        )
        (self.root / "llms.txt").write_text(
            "# Site\n<!-- PARENT-HUB:START -->\n<!-- PARENT-HUB:END -->", encoding="utf-8"
        )
        self.bundle = self.root / "content" / "production" / "2026-08-10-example"
        (self.bundle / "ARTICLE.md").write_text(
            "# Example Guide\n\n## What to notice\n\nA useful paragraph for parents.", encoding="utf-8"
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
            "schema_version": 1,
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
        self.assertIn("Example Guide", article.read_text(encoding="utf-8"))
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

    def test_pinterest_campaign_requires_every_pin_to_keep_utm_attribution(self):
        self.write_manifest(self.manifest())
        campaign = self.bundle / "PINTEREST.md"
        campaign.write_text("## Pin 1\n\n- Title: Missing attribution\n- Description: No link", encoding="utf-8")

        with self.assertRaisesRegex(PublicationError, "expected five titled pins"):
            validate_bundle(self.root, self.bundle / "PUBLISH.json")


if __name__ == "__main__":
    unittest.main()
