from django.template import loader
from django.http import HttpResponse

from wavepool.models import NewsPost
from wavepool.code_exercise_defs import code_exercise_defs, code_review_defs, code_design_defs
from django.conf import settings


def front_page(request):
    """ View for the site's front page
        Returns all available newsposts, formatted like:
            cover_story: the newsposts with is_cover_story = True
            top_stories: the 3 most recent newsposts that are not cover story
            archive: the rest of the newsposts, sorted by most recent
    """
    template = loader.get_template('wavepool/frontpage.html')
    top_stories_ordered = NewsPost.objects.all().order_by('-publish_date')
    # cover_story = top_stories_ordered[2]
    cover_story = NewsPost.objects.all().order_by('?').first()
    cover_story.body = cover_story.body.replace('<p>', '')
    cover_story.is_cover_story = True
    cover_story.save()
    top_stories = []
    other_stories = []
    # coverStoryInTopStory = False
    
    for story in top_stories_ordered:
        story.body = story.body.replace('<p>', '')
        if cover_story.pk == story.pk:
            continue
        elif(len(top_stories) < 3):
            top_stories.append(story)
        else:
            other_stories.append(story)

    context = {
        'cover_story': cover_story,
        'top_stories': top_stories,
        'archive': other_stories,
    }

    return HttpResponse(template.render(context, request))

# changed newspost to get the id of the num that's in the path
# to grab the correct newspost.
def newspost_detail(request, newspost_id=None):
    template = loader.get_template('wavepool/newspost.html')
    newspost = NewsPost.objects.get(pk=newspost_id)
    newspost.body = newspost.body.replace('<p>', '')

    context = {
        'newspost': newspost,
    }

    return HttpResponse(template.render(context, request))


def instructions(request):
    template = loader.get_template('wavepool/instructions.html')

    context = {
        'code_exercise_defs': code_exercise_defs,
        'code_design_defs': code_design_defs,
        'code_review_defs': code_review_defs,
        'show_senior_exercises': settings.SENIOR_USER,
    }
    return HttpResponse(template.render(context, request))
