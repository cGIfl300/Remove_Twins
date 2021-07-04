# Remove_Twins
I have many twins files (same content) inside a directory. They have the same name (begin).
I could remove them manualy but that will be too long.
Thus I created this script we can re-use and adapt to another purpose.
## Usage 
`remove_twins.py`  
Will remove all twin files, be carefull NO REVERSE!  
### Not deleting anything
`remove_twins.py --dry`  
Will simulate file removing. 
### Ignoring filesizes (stupid but I needed it)
`remove_twins.py --nosize`  
Will ignore filesizes. 