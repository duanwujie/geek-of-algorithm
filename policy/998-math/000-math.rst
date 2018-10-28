Math
============


欧拉公式证明
--------------------



.. math::
	e^{ix}=\cos x + i\sin x
	
	\because 
	
	e^x = 1 + \frac{x}{1!} + \frac{x^2}{2!} +  \frac{x^3}{3!} + \frac{x^4}{4!} + .....

	\sin x = x - \frac{x^3}{3!}  + \frac{x^5}{5!} - \frac{x^7}{7!} + ......
	
	\cos x = 1 - \frac{x^2}{2!}  + \frac{x^4}{4!} - \frac{x^6}{6!} + ......
	
	x \rightarrow ix
	
	i^3 = -i \qquad 
	i^4 = 1 \qquad 
	i^5 = i \qquad 
	i^6 = -1 \qquad 
	i^7 = -i \quad......
	
	e^{ix} = 1 + \frac{ix}{1!} + \frac{(ix)^2}{2!} +  \frac{(ix)^3}{3!} + \frac{(ix)^4}{4!} + .....
	
	e^{ix} = 1 + \frac{ix}{1!} - \frac{x^2}{2!} -  \frac{ix^3}{3!} + \frac{x^4}{4!} + .....
	
	e^{ix} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} + \frac{ix}{1!} -  \frac{ix^3}{3!} ..... 
	
	\therefore
	
	e^{ix} = \cos x + i\sin x
	
	x \rightarrow \pi
	
	e^{i\pi} = \cos pi + i\sin pi
	
	e^{i\pi} = -1 \rightarrow  e^{i\pi} + 1 = 0
	

