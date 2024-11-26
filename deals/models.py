from django.db import models
from django import forms

# Add these:
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


class DealsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        product_pages = self.get_children().live().order_by("-first_published_at")
        context["product_pages"] = product_pages
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]


# class BlogTagIndexPage(Page):

#     def get_context(self, request):

#         # Filter by tag
#         tag = request.GET.get('tag')
#         blogpages = BlogPage.objects.filter(tags__name=tag)

#         # Update template context
#         context = super().get_context(request)
#         context['blogpages'] = blogpages
#         return context


# class BlogPageTag(TaggedItemBase):
#     content_object = ParentalKey(
#         'BlogPage',
#         related_name='tagged_items',
#         on_delete=models.CASCADE
#     )


class ProductPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    specail_intro = models.CharField(max_length=250, blank=True)
    affiliate_link = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    body = RichTextField(blank=True)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Price (currency)",
        blank=True,
        null=True,
    )
    saving_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Saving Amount (currency)",
        blank=True,
        null=True,
    )
    free_return = models.BooleanField(default=False, verbose_name="Free Return")

    # tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
            ],
            heading="Blog information",
        ),
        FieldPanel("intro"),
        FieldPanel("specail_intro"),
        FieldPanel("body"),
        FieldPanel("affiliate_link"),
        FieldPanel("youtube_url"),
        FieldPanel("price"),
        FieldPanel("saving_amount"),
        FieldPanel("free_return"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]


class ProductPageGalleryImage(Orderable):
    page = ParentalKey(
        ProductPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]
