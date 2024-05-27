## 4 固体的电特性
### 4.11 
**推导热平衡状态下载流子的浓度：**

$`\left\{\begin{eqnarray}
	n_0 &= n_i \exp{\frac{E_F - E_{Fi}}{k_B T}} \\
	p_0 &= n_i \exp{\frac{E_{Fi} - E_F}{k_B T}}
\end{eqnarray}\right.`$

**其中，$`n_i`$为本征载流子浓度，$`E_{Fi}`$为本征Fermi能级。**

电子和空穴浓度可以表示为
$`\left\{\begin{eqnarray}
	n_0 &= N_- \exp{-\frac{E_c - E_F}{k_B T}} \\
	p_0 &= N_+ \exp{-\frac{E_F - E_v}{k_B T}}	
\end{eqnarray}\right.`$

对于本征半导体，有
$`\left\{\begin{eqnarray}
	n_i &=& N_- \exp{-\frac{E_c - E_{Fi}}{k_B T}} \\
	p_i &=& N_+ \exp{-\frac{E_{Fi} - E_v}{k_B T}} \\
	n_i &=& p_i
\end{eqnarray}\right.`$

因此，有
$`\left\{\begin{eqnarray}
	n_0 &= n_i \exp{\frac{E_F - E_{Fi}}{k_B T}} \\
	p_0 &= n_i \exp{\frac{E_{Fi} - E_F}{k_B T}}
\end{eqnarray}\right.`$




### 4.12
**在银材料的Hall效应实验中，银箔的厚度为$`0.05 \mathrm{\mu m}`$，磁场为$`1.25 \mathrm{T}`$，在其垂直方向上有$`20 \mathrm{mA}`$的电流通过时，产生的横向电势差为$`59 \mathrm{\mu V}`$。试计算Hall系数的数值。**

$`\begin{split}
	R &= \frac{E_y}{j_x B_z} \\
	  &= \frac{V_y / d_y}{B_z I_x / d_y d_z} \\
	  &= \frac{V_y d_z}{I_x B_z} \\
	  &= -0.85 \times 10^{-10} \mathrm{m}^3\mathrm{C}^{-1}
\end{split}`$






## 5 固体间接触的电特性
### 5.1 
**硅PN-结中的N-区施主杂质浓度为$`1 \times 10^{17}\mathrm{cm}^{-3}`$，P-区的受主杂质浓度为$`1 \times 10^{16} \mathrm{cm}^{-3}`$，试估算室温下PN-结的内建电势差。**

在N-区，有$`n \approx N_D = 1\times 10^{17}\mathrm{cm}^{-3}`$，其Fermi能级$`E_{F,N} = E_{Fi} + k_B T \ln{\frac{n}{n_i}}`$；

而在P-区，有$`p \approx N_A = 1\times 10^{16}\mathrm{cm}^{-3}`$，其Fermi能级$`E_{F,P} = E_{Fi} - k_B T \ln{\frac{p}{n_i}}`$；

所以PN-结的内建电势差$`V_D = \frac{E_{F,N}-E_{F,P}}{e} = \frac{k_B T}{e}\ln{\frac{np}{n_i^2}} = 0.75\mathrm{V}`$。




### 5.2
**硅PN-结的掺杂曲线如图所示，在室温零偏条件：**
1. 计算内建电势差$`V_D`$；
   $`\left(-\infty,0\right)`$是P-区，$E_{F,1} = E_{Fi} - k_B T \ln{\frac{N_1}{n_i}}$；

   $`\left(0,2\mathrm{\mu m}\right)`$是N-区，$E_{F,2} = E_{Fi} + k_B T \ln{\frac{-N_2}{n_i}}$；

   $`\left(2\mathrm{\mu m},+\infty\right)`$是N-区，$E_{F,3} = E_{Fi} + k_B T \ln{\frac{-N_3}{n_i}}$；

   在$`0`$处，$`V_{D,12} = \frac{E_{F,2}-E_{F,1}}{e} = \frac{k_B T}{e}\ln{\frac{-N_1 N_2}{n_i^2}} = 0.64\mathrm{V}`$，

   在$`2\mathrm{\mu m}`$处，$`V_{D,23} = \frac{E_{F,3}-E_{F,2}}{e} = \frac{k_B T}{e}\ln{\frac{N_2 N_3}{n_i^2}} = 0.03\mathrm{V}`$。


2. 画出平衡状态能带图。
   :framed_picture:





### 5.3
**A、B两种半导体材料形成理想异质结，A为P-Ge，B为N-GaAs，它们的基本常数为**

$`\begin{eqnarray}
	E_{g\mathrm{A}}=0.67\mathrm{eV}, E_{g\mathrm{B}}=1.43\mathrm{eV}, \\
	\chi_{\mathrm{A}}=4.13\mathrm{eV}, \chi_{\mathrm{B}}=4.06\mathrm{eV}, \\
	\delta_{\mathrm{A}}=\left(E_C-E_F\right)_{\mathrm{A}}=0.53\mathrm{eV}, \\
	\delta_{\mathrm{B}}=\left(E_C-E_F\right)_{\mathrm{B}}=0.1\mathrm{eV},
\end{eqnarray}`$

**求：**
1. 此异质结结构界面处的导带不连续量$`\Delta E_C`$、价带的不连续量$`\Delta E_V`$、接触电势差$`V_D`$别为多少？
   $`\begin{eqnarray}
		\Delta E_C &= \chi_A - \chi_B = 0.07\mathrm{eV}, \\
		\Delta E_V &= \left(E_{g,B}+\chi_B\right) - left(E_{g,A}+\chi_A\right) = 0.69\mathrm{eV}, \\
		V_D &= \frac{W_A - W_B}{e} = \frac{\left(\chi_A+\delta_A\right) - \left(\chi_B+\delta_B\right)}{e} = 0.50\mathrm{V}.
   \end{eqnarray}`$
   

2. 画出异质结的能带简图（要求画出带边变化趋势，标明$`\Delta E_C`$、$`\Delta E_V`$、$`V_D`$）。
   :framed_picture:





### 5.4
**考虑$`T=300\mathrm{K}`$时的硅PN-结二极管，参数如下：**

$`\begin{eqnarray}
	N_D=10^{18}\mathrm{cm}^{-3}, N_A=10^{16}\mathrm{cm}^{-3}, \\
	D_n=25\mathrm{cm}^{2}\mathrm{s}^{-1}, D_p=25\mathrm{cm}^{2}\mathrm{s}^{-1}, \\
	\tau_{n0} = \tau_{p0} = 1\mathrm{\mu s}, \\
	\text{横截面积}A=10^{-4}\mathrm{cm}^2,
\end{eqnarray}`$

确定以下偏压下的理想二极管电流：
1. 正偏$`0.5\mathrm{V}`$；
2. 反偏$`0.5\mathrm{V}`$。

$`L_p = \sqrt{D_p \tau_{p0}}, L_n = \sqrt{D_n \tau_{n0}},`$

$`N_{p0} = \frac{n_i^2}{N_D}, N_{n0} = \frac{n_i^2}{N_A},`$

$`J_s = e\left(\frac{D_n N_{p0}}{L_n} + \frac{D_p P_{n0}}{L_p}\right)`$

所以有

$`I_+ = J_s A \left(\exp{\frac{eV}{k_B T}}-1\right) = 4.4\times10^{-7} \mathrm{A}`$，

$`I_- = J_s A = 1.8\times10^{-15} \mathrm{A}`$。




### 5.5
**大致绘制出$`\text{Al}_{0.3}\text{Ga}_{0.7}`$As-GaAs突变异质结在下列情况下的能带图（假定$`\text{Al}_{0.3}\text{Ga}_{0.7}`$As的$`E_g=1.85\mathrm{eV}`$，GaAs的$`E_g=1.42\mathrm{eV}`$，$`\Delta E_C = 2/3\Delta E_g`$）：**
1. N-AlGaAs与本征GaAs；
   :framed_picture:


2. N-AlGaAs与P-GaAs；
   :framed_picture:


3. P-AlGaAs与N-GaAs。
   :framed_picture:





