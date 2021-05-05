from typing import List

from invenio_search import current_search_client


def _to_record(query_result) -> List:
    """Elasticsearch result to record
    """
    records = query_result['hits']['hits']

    return [r["_source"] for r in records] if records else []


def search_record_by_doi(identifier_doi: str) -> List:
    """Retrieves record using DOI identifier

    Args:
        identifier_doi (str): Record DOI Identifier
    Returns:
        List: List with query results
    """

    return _to_record(current_search_client.search(body={
        'query': {
            'bool': {
                'must': [
                    {
                        'match': {
                            'metadata.related_identifiers.scheme': 'doi'
                        }
                    },
                    {
                        'match': {
                            'metadata.related_identifiers.identifier': identifier_doi
                        }
                    }
                ]
            }
        }
    }))
