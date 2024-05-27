## 4 固体的电特性
### 4.1 外场中电子运动状态的变化
#### 4.1.1 波包和电子速度
不确定性关系$`\Delta r \Delta p \ge \frac{\hbar}{2}$或$\Delta r \Delta k \ge \frac{1}{2}`$

视为准经典粒子的条件：波包尺寸$`\frac{2\pi}{\Delta k} \gg a`$

平均速度（波包的群速度）$`\bar{v} = \frac{1}{\hbar} \frac{\mathrm{d}E}{\mathrm{d}k}`$


#### 4.1.2 加速度、有效质量、准动量
有效质量$`\frac{1}{m^*_{\alpha\beta}} = \frac{1}{\hbar^2} \frac{\partial^2E}{\partial k_\alpha \partial k_\beta}$，$\frac{1}{m^*_{\alpha}} = \frac{1}{\hbar^2} \frac{\partial^2E}{\partial k_\alpha^2}`$

准动量$`\hbar k`$


#### 4.1.3 恒定电场作用下电子的运动
⏳


#### 4.1.4 导体、绝缘体和半导体的能带论解释
满带和空带不导电，能带可导电
* 导体：满带-禁带-能带
* 非导体：满带-宽禁带-空带
* 半导体：满带-窄（$`E_g \lt 2\mathrm{eV}`$）禁带-空带

近满带，空穴$`\frac{1}{m^*} = -\frac{1}{m^*_e} = -\frac{1}{\hbar^2} \frac{\mathrm{d}^2E}{\mathrm{d}k^2}`$



### 4.2 金属中电子的输运过程
$`\sigma_0 = ne\mu`$



### 4.3 半导体中载流子的输运过程
#### 4.3.1 载流子浓度和Fermi能级
能量标度下的态密度$`N\left(E\right) = \frac{V}{2\pi^2} \left(\frac{2m}{\hbar^2}\right)^\frac{3}{2}E^\frac{1}{2}`$，其中$`m`$是有效质量，$`E`$是$`E - E_-`$

:hourglass_flowing_sand: 有效能级密度

:hourglass_flowing_sand: 载流子浓度

$`np = N_- N_+ \exp\left(-\frac{E_g}{k_B T}\right)`$:question:

$`np = n_i^2`$


#### 4.3.2 本征激发
$`n = p = n_i = \left(N_- N_+\right)^\frac{1}{2} \exp{-\frac{E_g}{2k_B T}}`$

本征半导体的费米能级近似地在带隙中央
$`\begin{split}
	E_{Ei} &= E_- - k_B T \ln\frac{N_-}{n_i} \\
	&= E_+ + k_B T \ln\frac{N_+}{n_i}
\end{split}`$
=⏳


#### 4.3.3 杂质与杂质激发
施主杂质（常温下）

$`n \approx N_D`$，$`p = \frac{n_i^2}{n}`$，$`E_F - E_{Fi} = k_B T \ln\frac{n}{n_i}`$

总杂质浓度$`N_{\mathrm{doping}} = N_A + N_D`$


#### 4.3.4 载流子的迁移及扩散
$`\sigma = ne\mu_- + pe\mu_+`$


#### 4.3.5 非平衡载流子
复合率$`R = \alpha_r np \approx \alpha_r n_i^2`$

:hourglass_flowing_sand: 准Fermi能级



### 4.4 Hall效应
Lorentz力$`\boldsymbol{F} = e\boldsymbol{v}\times\boldsymbol{B}`$

Hall系数$`R = \frac{1}{pe} = -\frac{1}{ne}`$

Hall电场$`E_H = vB = RjB`$




## 5 固体间接触的电特性
### 5.1 功函数与接触电势
电子亲和能$`\chi`$：电子真空能级到导带底的能量差，由材料本身的性质决定

热发射电流密度$`j = -q\frac{4\pi m\left(k_B T\right)^2}{\left(2\pi\hbar\right)^3}\exp{\frac{\chi-E_F}{k_B T}} \propto \exp{\frac{W}{k_B T}}`$，功函数$`W = \chi-E_F`$，从Fermi面发射电子

接触电势$`V_A-V_B = \frac{W_B-W_A}{e}`$