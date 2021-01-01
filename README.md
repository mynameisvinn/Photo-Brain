# ShowMe!
**ShowMe!** estimates an image's appeal ("instagrammability"). Its predictions could be used to sort a collection of images.

## Quickstart with Streamlit
```bash
streamlit run app.py  # navigate to browser
```
## Deploying on Heroku
Deploying the web app on Heroku can be done with the following:
```bash
git add .
git commit -m "heroku"
git push heroku master
heroku ps:scale web=1
```
## Testing
```bash
pytest .  # test
tox -e flake8

# or do everything in tox
tox
```