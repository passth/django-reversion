from reversion.views import create_revision
from reversion.conf import settings


class RevisionMiddleware:

    """Wraps the entire request in a revision."""

    manage_manually = False

    using = None

    atomic = True

    def __init__(self, get_response):
        self.get_response = create_revision(
            manage_manually=self.manage_manually,
            using=self.using,
            atomic=self.atomic,
            request_creates_revision=self.request_creates_revision
        )(get_response)

    def request_creates_revision(self, request):
        return request.method in settings.REVERSION_REQUEST_METHODS

    def __call__(self, request):
        return self.get_response(request)
