from django.contrib import admin
from django.urls import include, path
from magic_link import urls as magic_link_urls

from .redbox_core import info_views, auth_views, views

auth_urlpatterns = [
    path("magic_link/", include(magic_link_urls)),
    path("sign-in/", auth_views.sign_in_view, name="sign_in"),
    path(
        "sign-in-link-sent/",
        auth_views.sign_in_link_sent_view,
        name="sign-in-link-sent",
    ),
    path("signed-out/", auth_views.signed_out_view, name="signed_out"),
]

info_urlpatterns = [
    path("privacy-notice/", info_views.privacy_notice_view, name="privacy-notice"),
    path(
        "accessibility-statement/",
        info_views.accessibility_statement_view,
        name="accessibility-statement",
    ),
    path("support/", info_views.support_view, name="support"),
]

other_urlpatterns = [
    path("", views.homepage_view, name="homepage"),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("documents/", views.documents_view, name="documents"),
    path("upload/", views.upload_view, name="upload"),
    path("remove-doc/<str:doc_id>", views.remove_doc_view, name="remove_doc"),
    path("sessions/<str:session_id>/", views.sessions_view, name="sessions"),
    path("sessions/", views.sessions_view, name="sessions"),
]

urlpatterns = info_urlpatterns + other_urlpatterns + auth_urlpatterns
