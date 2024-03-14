# MusicBee to Navidrome Sync (MBNDS)

See [original](https://github.com/rombat/musicbee-navidrome-sync/blob/master/README.md) readme for context.

Replacing this because of changes for my personal workflow, just some personal notes here.

- Generate `MusicBee_Export.csv` with the same fields as the original with the addition of `Date Added`
  - Should look something like `"<File Path>","<Filename>","<Folder>","Title","Last Played","Play Count","Rating","Love","Skip Count","Date Added"`
- Get `navidrome.db` in the same way as the original
- Place both files in the root of this directory
- Run `npm run fullSync`
- Run `UpdateDates.py`

Done. `navidrome.db` is updated and ready to deploy.