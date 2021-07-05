# Remove_Twins
I have many twins files (same content) inside a directory. They have the same name (begin).
I could remove them manualy but that will be too long.
Thus I created this script we can re-use and adapt to another purpose.
## Usage as commandline
`remove_twins.py`  
Will remove all twin files, be carefull NO REVERSE!  
### Not deleting anything
`remove_twins.py --dry`  
Will simulate file removing. 
### Ignoring filesizes (stupid but I needed it)
`remove_twins.py --nosize`  
Will ignore filesizes. 
## Usage as Class
```python
from remove_twins import Remove_twins

app = Remove_twins(nosize = False) # By default, can be turned to true to ignore files sizes
app.dry() # Dry, don't remove anything.
app.remove() # Remove twin files, don't need dry call first.
```