# ShowMe!
**ShowMe!** estimates an image's popularity or instagrammability. Its predictions could be used to sort and rank a collection of images.

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
pytest .
```