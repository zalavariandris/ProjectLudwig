# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:05:12 2020

@author: andris
"""

import pandas as pd


df = pd.read_excel("ikon.xlsx", index_col=0)

#%% Drop duplicate exhibitions
"""
These exhibtions are duplicated in the Ikon archive.
i.e.:
- ARTFORT FESZTIVÁL, GENIUS LOCI
- "Nem is a föld miatt, nem is az ég miatt" (Apollinaire)
- &#8222;Bestia bestia látlak&#8221; - A Bizottság-kiállításhoz kapcsolódó filmklub
- (H)arcok. Dunaújvárosi művészek önmagukról - előadás
- ...bárányok a folyónál
- TÜKÖR: Hiroshi Teshigahara: A másik arca (Tanin no kao) filmvetítés Varró Attila filmesztéta előadásával
- UTÓSZEZON: Torino Frankfurt, Kassel, Sao Paulo - vetítések, előadások, beszélgetések
"""
duplicates = df[df.duplicated(subset=['title', 'date', 'gallery', 'artists'], keep=False)]
df.drop_duplicates(subset=['title', 'date', 'gallery', 'artists'], keep='first')
