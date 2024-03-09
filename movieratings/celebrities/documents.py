from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl_drf.filter_backends import SuggesterFilterBackend, DefaultOrderingFilterBackend, \
    OrderingFilterBackend, FilteringFilterBackend, SearchFilterBackend, CompoundSearchFilterBackend, \
    FunctionalSuggesterFilterBackend
from django_elasticsearch_dsl_drf.pagination import LimitOffsetPagination
from elasticsearch_dsl import analyzer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf import constants
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from tv_shows.documents import TVShowDocumentViewSet
from .models import Celebrity
from .serializers import CelebritiesSerializer

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)


@registry.register_document
class CelebritiesDocument(Document):

    id = fields.IntegerField(
        attr="id",
    )
    name = fields.TextField(
        fielddata=True,
        attr='name', analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', )
        }
    )
    slug = fields.TextField(
        fielddata=True,
        attr='slug', analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword')
        }
    )
    birth_country = fields.ObjectField(
        properties={
            'name': fields.TextField(
                analyzer=html_strip,
                fields={
                    'raw': fields.KeywordField(),
                    'suggest': fields.CompletionField(),
                }
            )
        }
    )
    birth_date = fields.DateField(attr='birth_date', )
    occupations = fields.ObjectField(
        properties={
            'name': fields.TextField(
                multi=True,
                analyzer=html_strip,
                fields={
                    'raw': fields.KeywordField(multi=True),
                    'suggest': fields.CompletionField(multi=True),
                }
            )
        }
    )

    class Index:
        name = 'celebrities'
        settings = {
            'number_of_shards': 1, 'number_of_replicas': 0
        }

    class Django:
        model = Celebrity


class CelebritiesDocumentViewSet(DocumentViewSet):
    document = CelebritiesDocument
    serializer_class = CelebritiesSerializer
    lookup_field = 'slug'
    pagination_class = LimitOffsetPagination
    filter_backends = (
        SuggesterFilterBackend,
        FilteringFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
        CompoundSearchFilterBackend,
        FunctionalSuggesterFilterBackend,
    )
    search_fields = {
        'name': {'fuzziness': 'AUTO'},
        'slug': {'fuzziness': 'AUTO'}
    }
    ordering_fields = {
        'name': 'name',
        'birth_date': 'birth_date',
    }
    ordering = ('birth_date', 'name')
    filter_fields = {
        'occupations': {
            'field': 'occupations',
            'lookups': (
                constants.LOOKUP_FILTER_TERMS,
                constants.LOOKUP_FILTER_PREFIX,
                constants.LOOKUP_FILTER_WILDCARD,
                constants.LOOKUP_QUERY_IN,
                constants.LOOKUP_QUERY_EXCLUDE,
            )
        },
        'occupations.raw': {
            'field': 'occupations.raw',
            'lookups': (
                constants.LOOKUP_FILTER_TERMS,
                constants.LOOKUP_FILTER_PREFIX,
                constants.LOOKUP_FILTER_WILDCARD,
                constants.LOOKUP_QUERY_IN,
                constants.LOOKUP_QUERY_EXCLUDE,
            )
        },
        'birth_date': 'birth_date',
        'birth_country': {
            'field': 'birth_country',
            'lookups': (
                constants.LOOKUP_QUERY_IN,
                constants.LOOKUP_QUERY_EXCLUDE,
            )
        },
    }

    suggester_fields = {
        'name_suggest': {
            'field': 'name.suggest',
            'suggesters': [
                constants.SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 5,
                'skip_duplicates': True,
            },
        },
        'slug_suggest': {
            'field': 'slug.suggest',
            'suggesters': [
                constants.SUGGESTER_COMPLETION,
            ],
            'options': {
                'size': 5,
                'skip_duplicates': True,
            },
        },
    }

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        data = [instance.to_dict() for instance in queryset]

        return Response(data, status=status.HTTP_200_OK)
