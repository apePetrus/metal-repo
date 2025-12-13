# metal-repo: The Personal Metal Archive

A repository to log metal albums, rate songs, comment reviews and keep track of
your metal taste.

---

## Project status

- MVP under development

## Technologies

- Python/Flask
- SQLite3
- Jinja

## Installation setup

- TBA

## Features

- Register bands and albums
- Rate bands, albums and songs
- Keep track of what you are currently listening to
- Log what you are planning to listen to

---

## Roadmap

### 1. Feature: bands

- [ ] Finish the registration form
- [ ] Implement edit route (PUT/PATCH)
- [ ] Implement delete route (DELETE)

### 2. Feature: albums & tracks

- [ ] Model and create tables for albums and tracks
- [ ] Create a rendering table and a form to log albums (name, year, cover, and
a link to the band)
- [ ] Create a feature to add musics to an album
- [ ] Finish the route for listing albums

### 3. Feature: rating

- [ ] Add columns for rating and description on albums and track tables
- [ ] Finish the feature to the user to rate albums (1-10)
- [ ] Finish the feature to the user to rate songs (individually)
- [ ] Finish the logic to calculate the average album ranting based on songs
- [ ] Make possible to rate artists/bands
- [ ] Add a feature to register ratings and personal reviews about genres/albums

### 4. Feature: user lists

- [ ] Create table to manage personal lists
- [ ] Let user to add albums to a "Listened To" list
- [ ] Let user to add albums to a "Plan to Listen" list

### Infrastructure/General improvements tasks

- [ ] Restructure the project's directories (backend/frontend/database) to
better management

---

## Progress log and development history

Check progress log, development history and the old to-do list regarding
the initial development phases of the project on [PROGRESS_LOG](/PROGRESS_LOG.md)
