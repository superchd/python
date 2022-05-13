## 이차원 리스트 만들기 잘안됨 

1. xy_points[i]에 1을 넣고, 그다음 xy_h에 xy_points[i]를 넣으면 잘 구현이 안된다

```python

for i in range(xy_size[0]):
        np.append(xy_points[i], 1)
        np.append(xy_h, xy_points[i])
        
```

2. 반대로, xy_points[i]
