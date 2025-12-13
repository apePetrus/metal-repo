# Progress log

---

## Development history

### Infrastructure/General improvements tasks

- [x] Restructure the project's directories (backend/frontend/database) to
better management

Using the repository pattern, separating directories on their specific usage.

---

## Historical archival: initial development phase

Below is the to-do list used to start the initial development phase of the project

## First things first band to-do list

- [x] Simple CRUD to append a band name from a form to a variable
- [x] Route form submit to a POST route on Flask and return back to index
- [x] Basic HTML to render bands table
- [x] Add origin country field
- [x] Add genre field
- [x] Make a way to add multiple genres
- [x] Add activity status field
- [x] Create simple table on SQLite to store those info
- [x] For SQLite FK enforcements, run ```PRAGMA foreign_keys = ON```
- [x] Create enum file for band table fgstatus column
- [x] Create a method to get band genres and concatenate them into one string

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
