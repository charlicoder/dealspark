# from gcloud_tasks.decorators import task
from celery import shared_task
from analytics.models import Visitors


@shared_task
def test_celery_task(n):
    """Fetch social profile from full contact api"""
    for i in range(n):
        print(f"celery is running {i}")


@shared_task
def visitors_tracking(data):
    path = data.get("path")
    filtered_paths = ["/admin/", "/static/", "/media/"]
    is_match = any(filter_path in path for filter_path in filtered_paths)
    if not is_match:
        visitor = Visitors(**data)
        visitor.save()
