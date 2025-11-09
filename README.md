# metal-repo

A repository to log metal albums, rate songs, comment reviews and keep track of
your personal metal taste.

## To-do

- Create bands entries
- Create albums entries and being able to add musics to those albums
- List bands and albums
- Add albums to a "Listened to" list
- Rate album from 1 - 10;
- Rate songs individually;
- Make an average rate from the album based on each songs score(?)
- Add albums to a "Plan to listen" list
- Rate artists
- Take notes to most liked metal genres, most liked albums, most liked bands

## First things first band to-do list

- [x] Simple CRUD to append a band name from a form to a variable
- [x] Route form submit to a POST route on Flask and return back to index
- [x] Basic HTML to render bands table
- [ ] Add origin country field
- [ ] Add genre field
- [ ] Make a way to add multiple genres (select and append to an array?)
- [ ] Add activity status field (input of type select)
- [x] Create simple table on SQLite to store those info
- [x] For SQLite FK enforcements, run ```PRAGMA foreign_keys = ON```
- [ ] Create enum file for band table fgstatus column
- [ ] Create a method to get band genres and concatenate them into one string

### band table

- [x] cdband integer primary key
- [x] nmband varchar(50) not null
- [x] cdcountry integer -- Must map to country.cdcountry
- [x] fgstatus integer --  1 (active), 2 (split-up), 3 (changed name), 4 (unknown)

### country table

- [x] cdcountry integer primary key
- [x] nmcountry varchar(50) not null

### genre table

- [x] cdgenre integer primary key
- [x] nmgenre varchar(20) not null

### bandgenre table

- [x] cdband integer not null -- Must map to band.cdband
- [x] cdgenre integer not null -- Must map to genre.cdgenre
