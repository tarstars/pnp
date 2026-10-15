# Related literature and version comparison

Checked on **15 October 2026**. This collection accompanies the focused review of Topchyi's proposed proof. It is **not a collection of verified repairs**: mathematical background, a later posting, and a rigorous continuous-computation framework are kept distinct.

The original manuscript in `paper/`, its stable text extraction, the claims ledger, and the existing verdict are unchanged by this addition.

## Index

| Source | Role | Repository copy / access |
|---|---|---|
| Topchyi, *The Theory of Plafales: P vs NP Problem Solution*, Preprints.org v4 (15 September 2026) | Version comparison with the uploaded 11 September manuscript | [Source PDF; not archived](https://www.preprints.org/frontend/manuscript/54550dfca2a8fc65314fc16a95f40bc5/download_pub), CC BY 4.0; [source](https://www.preprints.org/manuscript/202603.0689/v4) |
| Topchyi, *Quadruple Role of the Basis Functions of Serendipity Finite Elements. Review of the Results* (2016) | Finite-element / CTSA background; reference [5] of the reviewed paper | [English PDF](pdfs/topchyi_2016_serendipity_review_en.pdf), CC BY 4.0; [journal record](https://works.vntu.edu.ua/index.php/works/article/view/474) |
| Stepanets' and Shydlich, *On One Extremal Problem for Positive Series* (2005) | Approximation-theory dependency [26] | Links only: [English publisher record](https://doi.org/10.1007/s11253-006-0042-4), [original journal](https://umj.imath.kiev.ua/index.php/umj/article/view/3718), [Ukrainian PDF landing page](https://umj.imath.kiev.ua/index.php/umj/article/view/3718/4161) |
| Gerasimenko and Gapyak, *Advances in Theory of Evolution Equations of Many Colliding Particles* (2023) | BBGKY / correlation background; dependency [28] | [67-page arXiv v1 PDF](pdfs/gerasimenko_gapyak_2023_colliding_particles_arxiv_v1.pdf), CC0 1.0; [record](https://arxiv.org/abs/2308.04143v1) |
| Bournez, Graca and Pouly, *Polynomial Time Corresponds to Solutions of Polynomial Ordinary Differential Equations of Polynomial Length* (ICALP 2016) | A rigorous model relating polynomial-time computation and polynomial ODEs | [15-page conference PDF](pdfs/bournez_graca_pouly_2016_polynomial_odes_icalp.pdf), CC BY 3.0; [publisher record](https://doi.org/10.4230/LIPIcs.ICALP.2016.109) |
| Bournez, Graca and Pouly, same main title (JACM 2017) | Extended treatment of the preceding framework | Links only: [journal DOI](https://doi.org/10.1145/3127496), [author manuscript v3](https://arxiv.org/abs/1609.08059v3) |
| Topchyi, *The Theory of Plafales. P vs NP Problem Solution, Bridge* (December 2024) | Earlier claim; unresolved retrieval target | [ResearchGate record](https://www.researchgate.net/publication/386322806_THE_THEORY_OF_PLAFALES_P_VS_NP_PROBLEM_SOLUTION_Bridge); no file available |

BibTeX: [related_articles.bib](related_articles.bib). Machine-readable metadata and license evidence: [related_articles.json](related_articles.json). The original paper's complete reference list remains in [bibliography.md](bibliography.md).

## Relevance and limits

### The later posting: Topchyi v4

The source labels v4 as not peer-reviewed. It is a later **posting**, not assumed to be a substantive correction. Its printed page 14 (PDF page 15, after the cover) retains the fractional-power mean identity as **Corollary 2**, followed by an omitted proof. The same identity appears as equation (2) of system U. The checked-in September manuscript calls it **Corollary 5.4**. That page also retains the assertion about identifying unchecked instances after checking the first M.

**Review inference:** the later posting does not repair those specific steps. The numerical counterexample in the existing review concerns the claimed implication between the mean identities; it is not a counterexample satisfying every condition of the entire system U. This collection does not re-audit every statement in v4.

### Supporting mathematics

The 2016 Topchyi article reviews serendipity basis construction and time-dependent field models. Its pages 3-4 discuss basis-selection tasks and software for temperature-field rendering. **Review inference:** this supplies context for the geometric representation, not a verified algorithm that computes unknown SAT labels.

For Stepanets'-Shydlich, the publisher and original-journal abstracts describe extremal problems for products of nonnegative sequences and n-term approximation. **Access qualification:** the English full text was not obtained. An official Ukrainian-PDF link was located during this addition, but its binary retrieval and full text were not verified. This is more precise than saying that no full-text route exists. No theorem-level claim is made about unseen material.

The Gerasimenko-Gapyak paper studies evolution equations for hard-sphere systems, the BBGKY hierarchy, correlations, and kinetic descriptions. The archived file is specifically the **67-page arXiv v1**, not a claim to be byte-identical to the journal printing on pages 729-804. It is relevant background for the physical model; no polynomial-time SAT reduction has been verified from it in this collection. Reference [27], Gerasimenko-Shtyk (2008), remains listed in the original bibliography and is not silently replaced by [28].

### A rigorous comparison framework, not a SAT solver

The Bournez-Graca-Pouly work relates polynomial-time computation to an explicitly defined polynomial-ODE model. Its computational resource is solution-curve length, with input encoding and reliable output conditions, rather than merely the time parameter of an arbitrary dynamical system.

**Review inference:** this illustrates the kind of bridge that a continuous SAT algorithm would need. It does not validate Topchyi's system, prove that it meets those hypotheses, or supply a polynomial-time SAT solver. The conference paper and the extended journal version have separate records.

### Unavailable earlier preprint

The December 2024 *Bridge* record offers a request to the author and states that no file is available. Its full text has not been reviewed. Its title and abstract alone do not justify concluding either that it fixes the problems or that it repeats them.

## Copies, attribution, and verification

All mirrored PDFs are unmodified source bytes with original notices retained. Copyright/license information belongs to the respective authors and publishers; these papers are not relicensed under any repository software license.

- Topchyi v4: Dmytro Topchyi; [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), stated by [Preprints.org](https://www.preprints.org/manuscript/202603.0689/v4).
- Topchyi 2016: D. O. Topchyi; first published in *Scientific Works of Vinnytsia National Technical University*, issue 2; [journal open-access policy](https://works.vntu.edu.ua/index.php/works/Open_access_policy) permits reuse under CC BY 4.0. The English PDF has internal pages 1-7; the reviewed paper cites pages 72-78.
- Gerasimenko-Gapyak arXiv v1: V. I. Gerasimenko and I. V. Gapyak; the [version's license link](https://arxiv.org/abs/2308.04143v1) specifies [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
- Bournez-Graca-Pouly ICALP: Olivier Bournez, Daniel S. Graca and Amaury Pouly; [DROPS record](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ICALP.2016.109) specifies [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/).

Link-only status is not a claim that a work is unavailable everywhere. For the extended Bournez manuscript, arXiv's non-exclusive distribution license is not treated as a general third-party redistribution license. For the other link-only items, access or redistribution terms were not confirmed sufficiently to archive a PDF here.

The import validates PDF signatures, page counts and title markers, and records SHA-256 checksums and resolved download URLs in `pdfs/manifest.lock.json` and `pdfs/SHA256SUMS`. Once imported, reproduce/verify with Python 3.10+ and Poppler:

```sh
python3 scripts/fetch_related_articles.py
(cd refs/pdfs && sha256sum --check SHA256SUMS)
```

Run these commands from the repository root. Existing locked PDFs must match their recorded checksum; an upstream replacement is not silently accepted. The original manuscript and its citation line numbers are never regenerated by this script.

**Import access note (15 October 2026):** Preprints.org returned HTTP 403 to the GitHub-hosted importer. The v4 PDF is therefore linked, not archived. Its license and the limited comparison above remain documented separately from this download failure.
