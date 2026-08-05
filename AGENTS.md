# Repository rules

## Golden rule — no employer information in this repository

This is a **personal, public** repository. It must contain **no information about the
user's employer** and **no reference to the user's work account**.

Never add, and always remove on sight:

- The employer's name or trademarks, in any file (prose, code, comments, commit
  messages, filenames, binary documents such as `.pptx`/`.docx`, image assets).
- The employer's product, tool, or internal-language names (proprietary toolchains,
  specification languages, internal file formats).
- Work email addresses, internal hostnames, internal git remotes, internal URLs,
  ticket IDs, project or customer names, or any other internal identifier.
- Customer, station, or project data originating from work.

If the employer's name is genuinely needed for a sentence to make sense, write **`P`**.
For product or language names, genericize instead (e.g. "a formal specification
language", "an interlocking toolchain") — a single-letter substitute does not read.

Only the personal identity `ronggufly@gmail.com` may appear as author or contact.

Before committing, scan the staged diff for the employer name, its email domain, and
internal hostnames — the rule deliberately does not spell them out here, since naming
them would itself violate it:

```bash
git diff --cached | grep -inE "<employer-name>|<employer-domain>|<internal-host>"
```

Work-related knowledge belongs in a work repository, not here.
