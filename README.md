# ES-project
get data from [here](http://www.websudoku.com/)

## Sudoku_crawer.py
### usage
```
python Sudoku_crawer.py hardness howmany
```

| parameter | meaning | example |
| -------- | -------- | -------- |
| hardness  |   難度 </br> 1:  Easy </br> 2: Medium</br> 3:  Hard </br> 4:  Evil | 1    |
| howmany  |   要爬幾個    | 10     |

則會爬難度為hardness 的數獨 howmany 個。
命名為 `hardness_0.npy`  ...  `hardness_howmany.npy`
放在`./data/` 

### exmple
```
python Sudoku_crawer.py 2 10
```
則會爬難度為Medium 的數獨 10 個。
命名為 `Medium_0.npy`  ...  `Medium_10.npy`
放在`./data/` 
