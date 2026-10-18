# Repository maintenance

- Keep filenames, source identifiers, app labels, messages and documentation in English. Keep the neutral App Inventor namespace consistent across paths and project settings.
- Publish technical sources only. Never add participant identities, contact numbers, personal appendices, credentials, office documents, screenshots, prebuilt APKs or unreviewed videos.
- Preserve the sanitized AIA archive and matching editable source tree together. Rebuild and validate the archive whenever source files change.
- Run `python -m unittest discover -s tests -q` before committing and pushing verified changes to this repository's own origin. Do not build, install or execute the app, place calls or send SMS during offline checks.
- Keep local originals and the recovery ref private. Never rewrite history or force-push without explicit approval. Use CacheTide only when referring to that contributor; do not infer authorship or a license grant.
