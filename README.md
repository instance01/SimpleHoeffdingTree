## SimpleHoeffdingTree

Simply calculates the splits based on the amazing Hoeffding bound.
This is just for research purposes.

Reference paper:

```
@inproceedings{domingos2000mining,
  title={Mining high-speed data streams},
  author={Domingos, Pedro and Hulten, Geoff},
  booktitle={Proceedings of the sixth ACM SIGKDD international conference on Knowledge discovery and data mining},
  pages={71--80},
  year={2000}
}
```


Sample data:

| Person | Time since license | Gender | Area | Risk class |
| ------ | ------------------ | ------ | ---- | ---------- |
| 1|1 − 2|m|urban|low |
| 2|2 − 7|m|rural|high |
| 3|> 7  |f|rural|low |
| 4|1 − 2|f|rural|high |
| 5|> 7  |m|rural|high |
| 6|1 − 2|m|rural|high |
| 7|2 − 7|f|urban|low |
| 8|2 − 7|m|urban|low |



Sample output (with verbose set to True):

```
('1-2',)
('e', -0.0)
('w', 1, 2)
('2-7',)
('e', -0.0)
('w', 1, 2)
('weighted_sum', 0.0)
('infogain', 1.0, 0.0, ': ', 1.0)
('m',)
('e', 1.0)
('w', 2, 2)
('weighted_sum', 1.0)
('infogain', 1.0, 1.0, ': ', 0.0)
('urban',)
('e', -0.0)
('w', 1, 2)
('rural',)
('e', -0.0)
('w', 1, 2)
('weighted_sum', 0.0)
('infogain', 1.0, 0.0, ': ', 1.0)
('1-2',)
('e', 1.0)
('w', 2, 4)
('2-7',)
('e', -0.0)
('w', 1, 4)
('>7',)
('e', -0.0)
('w', 1, 4)
('weighted_sum', 0.5)
('infogain', 1.0, 0.5, ': ', 0.5)
('m',)
('e', 1.0)
('w', 2, 4)
('f',)
('e', 1.0)
('w', 2, 4)
('weighted_sum', 1.0)
('infogain', 1.0, 1.0, ': ', 0.0)
('urban',)
('e', -0.0)
('w', 1, 4)
('rural',)
('e', 0.9182958340544896)
('w', 3, 4)
('weighted_sum', 0.6887218755408672)
('infogain', 1.0, 0.6887218755408672, ': ', 0.31127812445913283)
('1-2',)
('e', 0.9182958340544896)
('w', 3, 6)
('2-7',)
('e', -0.0)
('w', 1, 6)
('>7',)
('e', 1.0)
('w', 2, 6)
('weighted_sum', 0.792481250360578)
('infogain', 0.9182958340544896, 0.792481250360578, ': ', 0.12581458369391152)
('m',)
('e', 0.8112781244591328)
('w', 4, 6)
('f',)
('e', 1.0)
('w', 2, 6)
('weighted_sum', 0.8741854163060885)
('infogain', 0.9182958340544896, 0.8741854163060885, ': ', 0.044110417748401076)
('urban',)
('e', -0.0)
('w', 1, 6)
('rural',)
('e', 0.7219280948873623)
('w', 5, 6)
('weighted_sum', 0.6016067457394686)
('infogain', 0.9182958340544896, 0.6016067457394686, ': ', 0.31668908831502096)
('1-2',)
('e', 0.9182958340544896)
('w', 3, 8)
('2-7',)
('e', 0.9182958340544896)
('w', 3, 8)
('>7',)
('e', 1.0)
('w', 2, 8)
('weighted_sum', 0.9387218755408672)
('infogain', 1.0, 0.9387218755408672, ': ', 0.06127812445913283)
('m',)
('e', 0.9709505944546686)
('w', 5, 8)
('f',)
('e', 0.9182958340544896)
('w', 3, 8)
('weighted_sum', 0.9512050593046015)
('infogain', 1.0, 0.9512050593046015, ': ', 0.04879494069539847)
('urban',)
('e', -0.0)
('w', 3, 8)
('rural',)
('e', 0.7219280948873623)
('w', 5, 8)
('weighted_sum', 0.4512050593046014)
('infogain', 1.0, 0.4512050593046014, ': ', 0.5487949406953986)
All infogains: [(0.04879494069539847, 'gender'), (0.06127812445913283, 'time'), (0.5487949406953986, 'area')]
Split: area
```
