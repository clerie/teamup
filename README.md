# Teamup Calendar API

## Usage

Init teamup class

### `teamup` class

#### `__init__(teamup_token)`
```
t = teamup('<teamup_token>')
```
- `teamup_token`: You have to apply for a Teamup token before starting


#### `get(endpoint, payload={})`
```
r = t.get('<endpoint>', '<payload>')
```
- `endpoint`: Endpoint from Teamup API
- `payload`: GET request payload as dict

### `teamup_calendar` class

[...]

## TO DO
- Exception handling
- Write access
- Put everything in ONE class
