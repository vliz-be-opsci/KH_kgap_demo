from pykg2tbl import DefaultSparqlBuilder, KGSource, QueryResult
from pathlib import Path
from pandas import DataFrame
import os

# SPARQL EndPoint to use - wrapped as Knowledge-Graph 'source'
WORKFLDR: Path =  Path(__file__).parent
EXPORTFILE=str( WORKFLDR / "20240418_dump-full.ttl")
KGS: KGSource = KGSource.build(EXPORTFILE)


TEMPLATES_FOLDER = str(WORKFLDR / "queries")
GENERATOR = DefaultSparqlBuilder(templates_folder=TEMPLATES_FOLDER)


def generate_sparql(name: str, **vars) -> str:
    """Simply build the sparql by using the named query and applying the vars"""
    return GENERATOR.build_syntax(name, **vars)


def _execute_to_df(src: KGSource, name: str, **vars) -> DataFrame:
    """Builds the sparql and executes, returning the result as a dataframe."""
    sparql = generate_sparql(name, **vars)
    result: QueryResult = src.query(sparql=sparql)
    return result.to_dataframe()


def execute_to_df(name: str, **vars) -> DataFrame:
    return _execute_to_df(KGS, name, **vars)


class ExternalEndPoint:
    def __init__(self, src: KGSource):
        self.src = src
    
    def execute_to_df(self, name: str, **vars) -> DataFrame:
        return _execute_to_df(self.src, name, **vars)