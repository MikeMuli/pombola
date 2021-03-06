import itertools
import re

from django.conf import settings
from django.utils import unittest
from django.test.client import Client
from django.test.utils import override_settings
from django.test import TestCase, Client

from nose.plugins.attrib import attr

from .models import InfoPage

class InfoTest(TestCase):

    def setUp(self):
        pass

    def test_get_absolute_url(self):
        page = InfoPage(slug="page", title="Page Title", markdown_content="blah", kind=InfoPage.KIND_PAGE)
        post = InfoPage(slug="post", title="Post Title", markdown_content="blah", kind=InfoPage.KIND_BLOG)

        self.assertEqual(page.get_absolute_url(), "/info/page")
        self.assertEqual(post.get_absolute_url(), "/blog/post")


    @attr(country='south_africa')
    def test_info_newsletter_uses_custom_template(self):

        # Create the page entry so that we don't just get a 404
        InfoPage.objects.create(slug="newsletter", title="Newsletter", markdown_content="Blah blah")

        # Get the page
        c = Client()
        response = c.get('/info/newsletter')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "south_africa/info_newsletter.html")

    @override_settings(INFO_PAGES_ALLOW_RAW_HTML=True)
    def test_blog_raw_html(self):
        danger_post = InfoPage.objects.create(
            slug="danger",
            title="Visualization",
            raw_content='''<h1 class="foo">Hello there</h1>
                <script>alert('hi!');</script>
                <p>blah blah, unclosed paragraph
                <iframe></iframe>
                <div>And then a div...</div>''',
            use_raw=True,
            kind=InfoPage.KIND_BLOG,
        )
        try:
            # For reasons I don't understand, on Travis the result of
            # this has no space between '</script>' and '<p>' but not locally...
            as_html = re.sub(r'(?ms)\s+', ' ', danger_post.content_as_html)
            as_html = re.sub(r'</script><p>', '</script> <p>', as_html)
            self.assertEqual(
                as_html,
                "<div><h1 class=\"foo\">Hello there</h1> <script>alert('hi!');</script> <p>blah blah, unclosed paragraph <iframe/> </p><div>And then a div...</div></div>"
            )
            self.assertEqual(
                re.sub(r'(?ms)\s+', ' ', danger_post.content_as_cleaned_html),
                "<div><h1 class=\"foo\">Hello there</h1> <p>blah blah, unclosed paragraph </p><div>And then a div...</div></div>"
            )
            self.assertEqual(
                re.sub(r'(?ms)\s+', ' ', danger_post.content_as_plain_text),
                "Hello there blah blah, unclosed paragraph And then a div..."
            )
        finally:
            danger_post.delete()


class InfoBlogClientTests(TestCase):
    fixtures = ['sample_blog_posts.json']

    # def test_show_loaded_pages(self):
    #     pages = InfoPage.objects.all()
    #     if len(pages):
    #         for page in pages:
    #             print page
    #     else:
    #         print "no pages found"

    def _test_label(self, tests, url_base):
        c = Client()

        all_contents = list( itertools.chain( *tests.values() ) )
        # print all_contents

        for label, expected_contents in tests.items():
            url = url_base + label
            # print '------------------', url
            response = c.get(url)
            for content in expected_contents:
                # print label, "should contain", content
                self.assertContains(response, content)

            for content in all_contents:
                if content in expected_contents: continue
                # print label, "should not contain", content
                self.assertNotContains(response, content)

    @attr(country='south_africa')
    def test_tags(self):
        self._test_label(
            tests = {
                "birds":   ["Blah Raven blah", "Blah Swan blah"],
                "mammals": ["Blah Black Panther blah", "Blah Polar Bear blah"],
            },
            url_base = '/blog/tag/'
        )

    @attr(country='south_africa')
    def test_categories(self):
        self._test_label(
            tests = {
                "category-1": ["Blah Raven blah", "Blah Polar Bear blah"],
                "category-2": ["Blah Black Panther blah", "Blah Swan blah"],
            },
            url_base = '/blog/category/'
        )

