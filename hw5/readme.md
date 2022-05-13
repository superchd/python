## 이차원 리스트 만들기 잘안됨 

1. xy_points[i]에 1을 넣고, 그다음 xy_h에 xy_points[i]를 넣으면 잘 구현이 안된다

```python

for i in range(xy_size[0]):
        np.append(xy_points[i], 1)
        np.append(xy_h, xy_points[i])
        
```

<img width="256" alt="스크린샷 2022-05-13 오후 3 22 45" src="https://user-images.githubusercontent.com/63406434/168223305-592eab8a-1a70-4e88-9ecc-7a88eef16702.png">

행렬에 append가 안되었다 ? 왜왜??? 

2. 반대로, xy_points[i]
