sample_mecab_word2vec
=====================

Python sample code to try MeCab and word2vec

## Usage
---
#### Construct MeCab dictionary
- for niconico data set (specifically for niconico dictionary header data)
- You can get data from [NII](http://www.nii.ac.jp/cscenter/idr/nico/nico.html)

```
python dicformat.py $IN_PATH $OUT_PATH
```

#### Parse sentences
- parse $IN_PATH sentences using MeCab

```
python corpus.py parse $IN_PATH $OUT_PATH
```

#### Vectorize by word2vec
- vectorize parsed sentences from $IN_PATH using word2vec
- save vectorized model to $OUT_PATH


```
python corpus.py vectorize $IN_PATH $OUT_PATH
```

#### Calcurate similar words
- load vectorized data from $IN_PATH
- calcurate words using words and "+" and "-"

```
python corpus.py calc $IN_PATH

```
```
please input formula(or "END"):king-man+woman
please input formula(or "END"):END
```
