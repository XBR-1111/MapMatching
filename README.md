# 路网匹配前期调研

## 问题定义（形式化）

来源于文献[1.5](https://github.com/XBR-1111/MapMatching/blob/master/paper/A%20Survey%20on%20Map-Matching%20Algorithms.pdf)

输入：trajectory, road network

输出：route

##### Trajectory

A trajectory Tr is a sequence of chronologically ordered spatial points Tr : p_1 → p_2 → ... → p_n sampled from a continuously moving object. Each point pi consists of a 2-dimensional coordinate < x_i , y_i >, a timestamp ti, a speed spd_i (optional) and a heading θ_i (optional). 

i.e.: pi =< x_i , y_i , t_i , spd_i , θ_i >

##### Road Network

A road network (also known as map) is a directed graph G = (V, E), in which a vertex v = (x, y) ∈ V represents an intersection or a road end, and an edge e = (s, e, l) is a directed road starting from vertices s to e with a polyline l represented by a sequence of spatial points.

##### Route

A route R represents a sequence of connected edges, i.e. R : e_1 → e_2 → ... → e_n, where e_i ∈ G.E(1 ≤ i ≤ n) and e_k.e = e_{k+1}.s.

##### Map-Matching

Given a road network G(V, E) and a trajectory Tr, the map-matching find a route MR_G(Tr) that represents the sequence of roads travelled by the trajectory.

## 文献整理

### 综述

| 链接    | 引用                                                         | 备注                                                         |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [1.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/Current%20map-matching%20algorithms%20for%20transport.pdf) | M. A. Quddus, W. Y. Ochieng, and R. B. Noland, “Current map-matching algorithms for transport applications: State-of-the art and future research directions,” Transp. Res. Part C Emerg. Technol., vol. 15, no. 5, pp. 312–328, 2007, doi: 10.1016/j.trc.2007.05.002. | 提出的分类标准geometric, probabilistic, topological, advanced |
| [1.2](https://github.com/XBR-1111/MapMatching/blob/master/paper/A%20critical%20review%20of%20real-time%20map-matching%20algorithms%20Current%20issues%20and%20future%20directions.pdf) | M. Hashemi and H. A. Karimi, “A critical review of real-time map-matching algorithms: Current issues and future directions,” Comput. Environ. Urban Syst., vol. 48, pp. 153–165, 2014, doi: 10.1016/j.compenvurbsys.2014.07.009. | 提出自己的分类方法，比较详细地介绍了多篇论文                 |
| [1.3](https://github.com/XBR-1111/MapMatching/blob/master/paper/%E8%B7%AF%E7%BD%91%E5%8C%B9%E9%85%8D%E7%AE%97%E6%B3%95%E7%BB%BC%E8%BF%B0_%E9%AB%98%E6%96%87%E8%B6%85.pdf) | 高文超,李国良,塔娜.路网匹配算法综述[J].软件学报,2018,29(02):225-250. | 问题定义、分类（基于[1]）、重点介绍HMM相关算法               |
| [1.4](https://github.com/XBR-1111/MapMatching/blob/master/paper/Comparative_Study_and_Application-Oriented_Classification_of_Vehicular_Map-Matching_Methods.pdf) | S.-I. Kubicka, Matej and Cela, Arben and Mounier, Hugues and Niculescu, “Comparative Study Classification of Vehicular and Application-Oriented Map-Matching Methods,” IEEE Intell. Transp. Syst. Mag., vol. 10, no. April 2018, pp. 150–166, 2018. | 从应用的角度进行分类                                         |
| [1.5](https://github.com/XBR-1111/MapMatching/blob/master/paper/A%20Survey%20on%20Map-Matching%20Algorithms.pdf) | P. Chao, Y. X. B, W. Hua, and X. Zhou, A Survey on Map-Matching Algorithms. Springer International Publishing, 2020. | 比较新的综述                                                 |

### 相似性模型（Similarity Model）

#### 基于距离（Distance-based）


| 链接      | 引用                                                         | 备注                                                |
| --------- | ------------------------------------------------------------ | --------------------------------------------------- |
| [2.1.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/An%20introduction%20to%20map%20matching%20for%20personal%20navigation%20assistants.pdf) | Bernstein D, Kornhauser A. An introduction to map matching for personal navigation assistants. Geometric Distributions, 1996,  122(7):1082−1083. | point-to-point，point-to-curve and curve-to-curve   |
| [2.1.2](https://github.com/XBR-1111/MapMatching/blob/master/paper/Some%20map%20matching%20algorithms%20for%20personal%20navigation.pdf) | White, Christopher E., David Bernstein, and Alain L. Kornhauser. "Some map matching algorithms for personal navigation assistants." *Transportation research part c: emerging technologies* 8.1-6 (2000): 91-108. | point-to-curve and curve-to-curve，实验比较四个算法 |
| [2.1.3](https://github.com/XBR-1111/MapMatching/blob/master/paper/Map%20matching%20by%20frechet%20distance%20and%20global%20weight%20optimization.pdf) | Wei, H., Wang, Y., Forman, G., Zhu, Y.: Map matching by frechet distance and global weight optimization. Technical Paper, Departement of Computer Science and Engineering p. 19 (2013) | 弗朗明歇距离                                        |

#### 基于模式（Pattern-based）

| 链接      | 引用                                                         | 备注                     |
| --------- | ------------------------------------------------------------ | ------------------------ |
| [2.2.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/Reducing_Uncertainty_of_Low-Sampling-Rate_Trajectories.pdf) | Zheng, K., Zheng, Y., Xie, X., Zhou, X.: Reducing uncertainty of low-sampling-rate trajectories. In: 2012 IEEE 28th International Conference on Data Engineering. pp. 1144–1155. IEEE (2012) | 从历史数据学习轨迹的模式 |

### 状态转移模型（State-Transition Model）

#### 隐马尔可夫模型（Hidden Markov Model，HMM）

| 链接      | 引用                                                         | 备注                                                         |
| --------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| [3.1.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/Map-Matching%20for%20Low-Sampling-Rate%20GPS%20Trajectories.pdf) | Lou Y, Zhang C, Zheng Y, Wang W, Huang Y. Map-Matching for low-sampling-rate GPS trajectories. In: Proc. of the ACM-GIS.  2009. 352−361. | ST-Matching 算法，高引（考虑车速）                           |
| [3.1.2](https://github.com/XBR-1111/MapMatching/blob/master/paper/An%20Interactive-Voting%20Based%20Map%20Matching%20Algorithm.pdf) | Yuan J, Zheng Y, Zhang C, Xie X, Sun JZ. An interactive-voting based map matching algorithm. In: Proc. of the MDM. 2010.  43−52. [doi: 10.1109/MDM.2010.14] | IVMM 算法，ST-Matching的改进，提出了新的result path search方法，效果好于ST-Matching |
| [3.1.3](https://github.com/XBR-1111/MapMatching/blob/master/paper/Hidden%20Markov%20Map%20Matching%20.pdf) | Newson P, Krumm J. Hidden Markov map matching through noise and sparseness. In: Proc. of the ACM-GIS. 2009.  336−343. [doi: 10.1145/1653771.1653818] | HMMM算法，状态转移矩阵与前两个不同，且给出了参数的经验值。包含了一个公开数据集 |
| [3.1.4](https://github.com/XBR-1111/MapMatching/blob/master/paper/Development%20of%20map%20matching%20algorithm%20for%20low%20frequency%20probe%20data.pdf) | Miwa T, Kiuchi D, Yamamoto T, Morikawaet T. Development of map matching algorithm for low frequency probe data.  Transportation Research Part C: Emerging Technologies, 2012,22(5):132−145. [doi: 10.1016/j.trc.2012.01.005] | Simplified HMM算法，速度快，性能略差于变种HMM                |
| [3.1.5](https://github.com/XBR-1111/MapMatching/blob/master/paper/Accurate%20real-time%20map%20matching%20for%20challenging%20environments.pdf) | Mohamed R, Aly H, Youssef M. Accurate real-time map matching for challenging environments. IEEE Trans. on Intelligent  Transportation Systems, 2017,18(4):847−857. [doi: 10.1109/TITS.2016.2591958] | OHMM算法，在线算法/增量算法                                  |
| [3.1.6](https://github.com/XBR-1111/MapMatching/blob/master/paper/Quick%20map%20matching%20using%20multi-core%20CPUs.pdf) | Song R, Lu W, Sun W, Huang W, Chen C. Quick map matching using multi-core CPUs. In: Proc. of the ACM-GIS. 2012.  605−608. [doi: 10.1145/2424321.2424428] | QMM快速算法，并行                                            |

#### 条件随机场（Conditional Random Field， CRF）

相比HMM，多考虑了观测之间的关系

| 链接      | 引用                                                         | 备注                                   |
| --------- | ------------------------------------------------------------ | -------------------------------------- |
| [3.2.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/The_Path_Inference_Filter_Model-Based_Low-Latency_Map_Matching_of_Probe_Vehicle_Data.pdf) | Hunter, T., Abbeel, P., Bayen, A.: The path inference filter: model-based low-latency map matching of probe vehicle data. IEEE Transactions on Intelligent Transportation Systems 15(2), 507–529 (2014) | online/offline，考虑限速和车辆驾驶模式 |

### 候选-进化模型（Candidate-Evolving Model，CEM）

当前的匹配不仅受到先前匹配结果的影响，而且还受到其他候选方案的影响。

#### 粒子滤波（Particle filter，PF）

| 链接      | 引用                                                         | 备注 |
| --------- | ------------------------------------------------------------ | ---- |
| [4.1.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/Multi-hypothesis%20map-matching%20using%20particle%20filtering.pdf) | Bonnifait, P., Laneurit, J., Fouque, C., Dherbomez, G.: Multi-hypothesis map-matching using particle filtering. In: 16th World Congress for ITS Systems and Services. pp. 1–8 (2009) |      |

#### 多假设方法（Multiple Hypothesis Technique，MHT）

与PF的区别：MHT根据一个评分函数来评估每个候选路边（或点），而不是试图近似邻接地图区域的复杂PDF。因此，MHT的计算成本被大大降低。

| 链接      | 引用                                                         | 备注 |
| --------- | ------------------------------------------------------------ | ---- |
| [4.2.1]() | Taguchi, S., Koide, S., Yoshimura, T.: Online map matching with route prediction. IEEE Transactions on Intelligent Transportation Systems 20(1), 338–347 (2018) |      |

### 评价模型（Scoring Model）

#### 简单权重（Naive weighting）

| 链接      | 引用                                                         | 备注           |
| --------- | ------------------------------------------------------------ | -------------- |
| [5.1.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/Matching%20GPS%20observations%20to%20locations%20on%20a%20digital%20map.pdf) | J. S. Greenfeld, “Matching GPS Observations to Locations on a Digital Map,” Transp. Res. Board, no. 3, p. 13, 2002. | 拓扑方法，高引 |

#### 模糊逻辑（Fuzzy Logic）

| 链接      | 引用                                                         | 备注                         |
| --------- | ------------------------------------------------------------ | ---------------------------- |
| [5.2.1](https://github.com/XBR-1111/MapMatching/blob/master/paper/A%20High%20Accuracy%20Fuzzy%20Logic%20Based%20Map%20Matching%20Algorithm%20for%20Road%20Transport.pdf) | O. W. Y. Quddus M A, Noland R B, “A high accuracy fuzzy logic based map matching algorithm for road transport,” J. Intell. Transp. Syst., vol. 10, pp. 103–115, 2006. | 模糊逻辑，输入包括方向和速度 |

## 计划实现的模型
1. S-Matching（ST-Matching忽略Temporal） 稳定健壮，实用性强，有成熟的研究和开源实现，可参考[python实现](https://github.com/xialeizhou/ST-matching)
2. IVMM 基于ST-Matching，效果好于ST-Matching，可参考[python实现](https://github.com/easysam/IVMM)
3. HMMM 从HMM角度出发的模型，可参考[python实现](https://github.com/caochuntu/KDD2021_guizu/tree/main/Map%20Matching)


## 数据集

可用于验证算法的效果以及作为数据结构的参考

| 命名    | paper链接                                                    | 数据集链接                                                   |
| ------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Seattle | [3.1.3](https://github.com/XBR-1111/MapMatching/blob/master/paper/Hidden%20Markov%20Map%20Matching%20.pdf) | [Seattle data](https://www.microsoft.com/en-us/research/publication/hidden-markov-map-matching-noise-sparseness/) |
| Global  |  [Global paper](https://github.com/XBR-1111/MapMatching/blob/master/paper/Dataset_for_testing_and_training_of_map-matching_algorithms.pdf)                                                            | [Global data](https://zenodo.org/record/57731#.YP55K8TitnI)  |
|         |                                                              |                                                              |



## 输入输出格式（proposal）

### 输入原子文件格式定义

| 文件名      | 内容                                             | 例子                                                         |
| ----------- | ------------------------------------------------ | ------------------------------------------------------------ |
| xxx.geo     | GPS samples & Vertexes of Road Network           | geo_id, type(Point), coordinates                             |
| xxx.usr     | user information(用于支持同一路网中匹配多条轨迹) | usr_id                                                       |
| xxx.rel     | road networks                                    | rel_id, type(geo), origin_id(geo_id), destination_id(geo_id) |
| xxx.dyna    | trajectory                                       | dyna_id,type(trajectory),time,entity_id(usr_id),location(geo_id), |
| config.json |                                                  |                                                              |

#### xxx.geo

包括GPS samples & Vertexes of Road Network

```
geo_id,type,coordinate
0,Point,"[-74.00313913822173,40.73359624463057]"
1,Point,"[-74.00612949321742,40.73581439418978]"
....
```

#### xxx.usr

若仅含有一条轨迹，则user_id只有1个人，否则user_id有多个人

```
usr_id
0
```

#### xxx.rel

用于表示路网的边，其中origin_id,destination_id表示xxx.geo中的Vertexes of Road Network。若道路双向通行，则应该包括两行。

```
rel_id,type,origin_id,destination_id
0,geo,0,1
1,geo,1,0
...
```

#### xxx.dyna

轨迹，其中location表示xxx.geo中的GPS samples，entity_id代表xxx.usr中的usr_id。推荐以entity_id为主关键字，time为第二关键字排序。

```
dyna_id,type,time,entity_id,location
0,trajectory,2012-04-03T14:00:09Z,0,2388
1,trajectory,2012-04-03T14:00:25Z,1,3921
2,trajectory,2012-04-03T14:02:24Z,2,20328
3,trajectory,2012-04-03T14:02:41Z,3,15114
4,trajectory,2012-04-03T14:03:00Z,4,23550
5,trajectory,2012-04-03T14:04:00Z,5,10589
6,trajectory,2012-04-03T14:04:38Z,6,6365
...
```

#### config.json

样例如下

```
{
    "geo":{
        "including_types":[
            "Point"
        ],
        "Point":{}
    },
    "usr":{
        "properties":{}
    },
    "rel":{
        "including_types":[
            "geo"
        ],
        "geo":{}
    },
    "dyna":{
        "including_types":[
            "trajectory"
        ],
        "trajectory":{
            "entity_id":"usr_id",
            "location": "geo_id",
        }
    },
    "info": {
        
  	}
}
```

### 输出格式定义

#### xxx.out

对于每一个GPS sample，需要一条路网与之对应，因而可定义与dyna_id对应的输出格式。

```
dyna_id,rel_id
0,2724
1,3419
2,341
...
```

### 扩展性说明

1. 对于轨迹数据，可选输入（如速度(speed)和方向(heading)）在dyna文件中添加相关的列用以说明
2. 对于路网数据，可选输入（如路段速度 in ST-Matching）在rel文件中添加相关的列用以说明
3. 对于输出数据，可选输出GPS矫正后位于路段上的地理坐标，可在输出文件中加入coordinate列



## 评价指标

用于构建模型时检验算法能否达到预期

## 相关技术参考

### GPS相关距离计算

* 两点之间大圆距离
* GPS点到路段的距离
* 参考http://www.movable-type.co.uk/scripts/latlong.html

