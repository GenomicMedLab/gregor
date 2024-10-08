"""Load VCFs into sqlite index."""

from pathlib import Path

from vrs_index_vcf._core import vcf_to_sqlite


def load_vcf(vcf_path: Path) -> None:
    """Load VRS-annotated VCF into sqlite database.

    :param vcf_path: path to VCF (must exist) to ingest
    """
    vcf_to_sqlite(vcf_path)
