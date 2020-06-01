# ES-project
> [time=Wed, May 27, 2020 6:52 PM]
> 
[TOC]

## Solver_RetGA.py
### usage
```
python Solver_RetGA.py QUESTION_NAME PRINT_FIT ITERATION ID
```

| parameter | meaning | example |
| -------- | -------- | -------- |
| QUESTION_NAME   | 題目名稱  </br> **\*** 檔案須為`.npy`  </br> **\*** 須放在`./data/` 下| Perfect_1   |
| PRINT_FIT   | 是否印出每個iteration 的fitness value  | 1  |
| ITERATION   | 最大ITERATION  | 50000  |
| ID | 輸出結果的id  | 0001     |

則會輸出以下檔案在`./save_result/`下

| name |  | 
| -------- | -------- | 
| `QUESTION_NAME_ID_RetGA.json`   | 儲存timecost 和 iteration  | 
| `QUESTION_NAME.npy`   | 儲存solution  | 

### exmple
```
python Solver_RetGA.py Perfect_1 1 50000 0001
```
則會輸出以下檔案在`./save_result/`下

| name |  | 
| -------- | -------- | 
| `Perfect_1_0001_RetGA.json`   | 儲存timecost 和 iteration  | 
| `Perfect_1.npy`   | 儲存solution  | 

## Sudoku_crawer.py
get data from [here](http://www.websudoku.com/)
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
