# sandbox

A playground for experiments, automations, and open-source exploration.

## Using openspec

This project uses [openspec](https://openspecindex.com) — the official Python client
for the OpenSpec Index API, which provides searchable specifications for
manufacturer parts with a source URL on every record.

Install the dependency:

```bash
pip install -r requirements.txt
```

Then run the example:

```bash
python3 openspec_example.py "316 stainless nylon insert lock nut"
```

No API key is required for the free tier. See https://openspecindex.com/docs
