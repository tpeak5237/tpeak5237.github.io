# Theerapat / Engineering Evidence

**An independent, public portfolio microsite for technical review.**

Live URL (when GitHub Pages finishes publishing): **https://tpeak5237.github.io/**

This is a standalone static site, built from scratch for public review. It is not the private `theerapat.org` source tree, a fork of private product code, or an official event website.

## Purpose

A reviewer should be able to understand the builder, inspect three real public repositories, open independent verification evidence, and distinguish implemented work from a future hackathon proposal in under two minutes.

## Public evidence selected

| Project | Source | Specific proof | Boundary |
| --- | --- | --- | --- |
| JaneQ | [Code](https://github.com/tpeak5237/janeq) | [Local test report (Oct 8)](https://github.com/tpeak5237/janeq/blob/main/docs/MAINTENANCE_VERIFICATION.md), [successful CI](https://github.com/tpeak5237/janeq/actions/runs/37784845264) | Static, browser-local utility; no physical camera or hosted runtime guarantee from CI |
| VideoOS | [Code](https://github.com/tpeak5237/VideoOS) | [Local test report (Oct 8)](https://github.com/tpeak5237/VideoOS/blob/main/docs/MAINTENANCE_VERIFICATION.md), [successful CI](https://github.com/tpeak5237/VideoOS/actions/runs/37784859294) | Local P0 CLI; not a deployed full AI video service; source lacks a project-level license |
| JongFood | [Code](https://github.com/tpeak5237/jongfood) | [PostgreSQL store](https://github.com/tpeak5237/jongfood/blob/main/src/server/postgres-store.mjs), [live-proof register](https://github.com/tpeak5237/jongfood/blob/main/LIVE_PROOF.md) | Real staging, production auth, and concurrent database behavior are not verified |

The site's **MistakeLoop** interaction is an explicitly labelled deterministic illustration of a proposed adaptive-learning idea, **not a working AI agent**, learning study, or hackathon submission.

## Local use

There are no build dependencies or runtime services.

```bash
python3 -m http.server 4173
# open http://localhost:4173
```

No remote fonts, scripts, images, analytics, API calls, forms, or cookies are used. Clicking project links navigates directly to the original public sources.

## Verification

```bash
python3 scripts/verify.py
```

The verification script checks critical structural landmarks, that the recorded evidence links and limitation labels remain visible, that no secrets or embedded third-party assets are present, and that the concept UI's declared branches exist. Optional manual checks: test 1440/800/390px viewports, keyboard focus, both concept buttons, and reduced-motion preferences. These are static-site checks, not security certification or proof that linked repositories are currently passing.

## Publication

This repository uses GitHub's special username Pages address. GitHub Pages must be configured to publish `main` from the root, or a suitable GitHub Actions workflow must be enabled by a repository administrator. A `pages` deployment cannot be inferred merely from a successful source push. Once published, verify the live URL independently.

## Privacy and provenance

- Only links and descriptions of **public** repositories are included.
- No private source, environment variables, confidential architecture, operational data, production database records, student records, user analytics, or credentials are included.
- The illustrations and code on this website are independently authored. No images or source code are copied out of private repositories.
- Test counts reflect the publicly documented October 8, 2026 verification snapshots, not continuous monitoring or customer usage.
- This is independent applicant work, not affiliated with OpenAI, Sea, or any hackathon organizer.

## License

The website source in this repository is licensed under MIT (see [`LICENSE`](LICENSE)). External projects retain their own licenses, including VideoOS's stated lack of a project-level license.
