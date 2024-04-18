from pykg2tbl import DefaultSparqlBuilder, KGSource, QueryResult
from pathlib import Path
from pandas import DataFrame
import os

# SPARQL EndPoint to use - wrapped as Knowledge-Graph 'source'
GDB_ENDPOINT: str = str(Path.cwd() / 
GDB: KGSource = KGSource.build(FILE_SOURCE)


TEMPLATES_FOLDER = str(Path().absolute() / "queries")
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
    """Builds the sparql and executes, returning the result as a dataframe."""
    return _execute_to_df(GDB, name, **vars)


class ExternalEndPoint:
    def __init__(self, src: KGSource):
        self.src = src
    
    def execute_to_df(self, name: str, **vars) -> DataFrame:
        return _execute_to_df(self.src, name, **vars)