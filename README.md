# San Francisco Ripe Fruit Finder 🍊

A web app that shows you which fruit-bearing street trees in San Francisco have ripe fruit right now!

## Features

- 🗺️ Interactive map of SF fruit-bearing street trees
- 🍎 Real-time ripeness status based on current month
- 🔍 Filter by fruit type (loquats, figs, apples, plums, cherries, etc.)
- 📍 View exact locations and addresses
- 📊 Live data from SF Open Data Portal (198K+ trees)

## Supported Fruits

The app tracks ripeness for:
- Loquats (Apr-Jun)
- Figs (Jun-Sep)
- Apples (Aug-Oct)
- Plums (Jun-Aug)
- Cherries (May-Jul)
- Pears (Aug-Oct)
- Persimmons (Oct-Dec)
- Apricots (Jun-Jul)
- Peaches (Jun-Aug)
- Olives (Oct-Dec)
- Citrus (varies by type)
- Mulberries (May-Jul)
- Walnuts (Sep-Oct)

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the app:
```bash
python app.py
```

3. Open your browser to: http://localhost:5000

## How It Works

1. **Backend (Flask)**: Fetches tree data from SF's Open Data API
2. **Fruit Detection**: Matches tree species names against known fruit trees
3. **Ripeness Logic**: Checks current month against typical ripening seasons
4. **Frontend**: Displays trees on interactive map with color coding (green = ripe, red = not in season)

## Data Source

Tree data comes from the [SF Street Tree List](https://data.sfgov.org/City-Infrastructure/Street-Tree-List/tkzw-k3nq) maintained by SF Public Works.

## Notes

- The app loads up to 5,000 trees from the API
- Ripeness dates are approximate based on typical SF seasons
- Always verify fruit is safe to eat before consuming
- Respect private property and only pick from public trees with permission

## License

Open source - use freely!
