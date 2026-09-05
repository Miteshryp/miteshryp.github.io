---
title: "Evolution of Computer Graphics"
date: "2023-11-14"
description: "Take a deep dive into the history of graphics softwares, programming and animations."
tags: ["graphics"]
author: "mitesh"
draft: false
---

Taking the ultra-realistic graphics commonly found in our modern digital interactions for granted has become extremely convenient for us. These graphics often enrich our experience and have allowed creative professionals such as screen-writers to explore the new and uncharted domains of their art. But have you ever wondered how this incredible world of User Experience and Graphics came into being? In this blog, we will learn about the story of how these ultra-realistic graphics have evolved over time when artists and computer scientists came together to lay its foundations!

{{< figure src="images/image-01.jpg" caption="A scene from the animated film “Moana”" >}}

{{< figure src="images/image-02.jpg" alt="Demonstration of CAD software" caption="Demonstration of CAD software used to create 3D designs." >}}

Although the line of the initial work in computer graphics is a big blur, the term “Computer Graphics” was first coined by William A Fetter when he made the first computer model of a human body while he was working as an Art Director at Boeing. The United States government was also using some primitive visualization techniques, which made some incremental steps in its development.

Computer Graphics is a critical component in modern digital human interfaces. It comprises applications from the field of data science and gaming to medical diagnosis. However, it did not start to take shape in the form we know until the early 1960s, when Ivan Sutherlands developed the SketchPad.

Sketchpad was a device capable of organizing geometric data of objects as points and modifying them using a “lightpen”. This is considered to be the ancestor of modern-day CAD software. Ivan Sutherlands was awarded with the Turing Award and Kyoto Prize for this project which he pursued during his PHd.

This was however a primitive technology primarily made for research purposes, and it wouldn’t be until the late 1970s when more advanced algorithms and hardware would be developed to support the requirements of the computer graphics projects in order to make them ready for the masses.

### Development of Animation Technology

The most awe-inspiring animated and motion graphics films use advanced software for producing sophisticated graphics animations. This software uses complex techniques under the hood to optimize graphics rendering and deliver the desired graphics fidelity in the movies that we see today. Let’s see how this complex innovation of technology came into existence.

Among the institutions such as MIT, Maryland, and many more that contributed to the foundational research into the field of computer graphics, the Ohio State University (OSU) made some unique contributions that would end up laying the foundational work for some of the most advanced computer graphics tools which would be used in large-scale animation studios.

The initial work done at OSU was primarily pioneered by Charles Csuri, an art professor at OSU who collaborated with professors in the mathematics department to explore the advances that a computing system can offer in his artistic creations. With their help, Prof. Csuri was able to produce some impressive results, comprising of a “sine curve man” image, and the “hummingbird in flight” which is considered to be the first computer animated artwork.

{{< figure src="images/image-03.png" caption="Sine Curve Man — Art work made by Charles Csuri" >}}

{{< figure src="images/image-04.png" caption="Hummingbird — Artwork by Charles Csuri considered to be the first animation in the world" >}}

In the following decade, the work at OSU took a more formal approach with funding from US government institutions such as the National Science Foundation (NSF) and the formation of the Computer Graphics Research Group (CGRG). This special research group in the OSU undertook several important projects such as GRASS, ANIMA, ANTS, etc which led to the development of several primitive tools, graphics pipeline architectures, standards and primitive algorithms used even in modern graphics processing applications. Tools such as specialized scripting languages for 3D graphics rendering, techniques encompassing keyframe animations, geometric modelling, real-time animation techniques, surface algorithms to alter meshes, and video storage systems are just a few examples of the result of these research projects which were nourished under the CGRG.

{{< figure src="images/image-05.jpg" caption="Skeletal animations used in Blender." >}}

To test the tools and techniques developed in the CGRG in the real world market, Charles Csuri shortly partnered with Robert Kunth of the Cranston Company to form a new company CCP (Cranston/Csuri Productions) during which they offered several kinds of computer-generated graphics to help companies develop innovative graphics for advertisements and promotions. This venture helped Csuri in transforming and polishing the technologies developed at the CGRG and making them suitable for industry use. Although Csuri eventually left the company to go back to work on ACCAD (CGRG was renamed to ACCAD — Advanced Computing Center for Arts and Design), the venture led to the addition of specialized tools such as utilities for character animation, rendering, modelling and adding post-production effects.

Development of such a rich ecosystem at the ACCAD group at OSU attracted rich graduate students which include some of the most recognizable names in the CGI industry. Industry giants such as Steve May (who served as the CTO at Pixar) and many more are a part of the rich alumni network of the ACCAD group, which played a crucial role in shaping the modern animation industry. Many of these techniques and algorithms continue to enable GPUs and several graphics intensive applications to carry out their critical functions.

### Graphics Development in Game’s Industry

Another crucial application of the advances in Computer Graphics came to be seen extensively in the video games industry. As of 2022, the worldwide market capital of the video game industry was $217.06 billion and is expected to reach $242.39 billion in the year 2023. The growth and achievement of the games industry can be credited to some crucial contributions made by some key players in the industry.

While OSU developed some crucial foundational algorithms for the field of computer graphics, pioneers like James Blinn and Edmin Catmull from the University of Utah made advanced contributions to the field of computer graphics which made techniques like textures, reflections and image rendering possible. These crucial innovations made at special interest groups like the ACM SIGGRAPH (which was the hub of state of the art innovations in computer graphics) shaped the techniques used in even the most basic game engines used nowadays. These techniques however needed to be implemented by utilizing the available hardware in the most optimized and structured way, and even further needed to be standardized to make the technical innovations possible.

The first initiative in this direction was made in 1977 with the preparation of the draft of **GKS** or the **Graphical Kernel System** , which was a standard for low-level graphics programming for 2D graphics applications. It provided several features for 2D vector graphic primitives and provided APIs and implementations that were standardized across various graphics platforms.

However, The first initiative for 3D graphics programming was made by the creation of a graphics programming framework called **PHIGS** , or **Programmers Hierarchical Interactive Graphics System** which took its inspiration from the GKS framework. This framework was considered the standard for 3D programming in the 1980s as it was supported by large graphics hardware vendors of the time such as IBM, Sun and DEC. PHIGS was however not very popular amongst the graphics application developers due to its lack of flexibility and configurability. It did not allow the programmers to modify the underlying implementations to optimize the application for their use cases.

To overcome this problem, Silicon Graphics (SGI) introduced the **IRIS Graphics Library (IRIS GL)** in 1981 to support the development of applications making use of low-level graphics on the SGI hardware which allowed developers to modify the implementation of graphics being handled on the hardware. The developers could for instance “cull” the objects to be rendered to eliminate the rendering of objects that are not visible in the screen on the CPU side before sending them over to the GPU, which allowed for major performance improvements in a time where hardware was already very limiting. This low-level nature of the IRIS GL resulted in mass adaptation of the framework in the development community.

![](images/image-06.png)

In 1991, In order to fight the decline of its user base, SGI released its graphics library as an open standard and formed an industry-wide consortium to standardize the framework and its specifications, which came to be known as OpenGL. This framework was compatible across many platforms due to the collaboration in the consortium and came to be adapted during the development of some famous games such as Quake and Doom. While the frameworks of tools and techniques for high quality graphics shifted from OpenGL to other tools over time, modifications of OpenGL (OpenGL ES) are still prominently used in many mobile devices and web based 3D graphics applications.

Over time, with the launch of more capable GPUs, the high end graphics applications came to adopt platform specific low-level graphics API such as DirectX for Windows and Metal for MacOS, which continue to drive the graphics industry to date. OpenGL was also deprecated and replaced by its successor Vulkan which had a much more modern API that resonated with modern graphics constructs.

Over time, with the launch of more capable GPUs, the high end graphics applications came to adopt platform specific low-level graphics API such as DirectX for Windows and Metal for MacOS, which continue to drive the graphics industry to date. OpenGL was also deprecated and replaced by its successor Vulkan which had a much more modern API that resonated with modern graphics constructs.

### The Rise of GPUs

As it goes without saying, the role of Graphics Processing Units cannot be ignored when it comes to Graphics Programming. For any engineer working in the field of software engineering or any technology enthusiast, it is no news that the advancement of GPUs has had a huge part in the development of modern Artificial Intelligence applications and techniques. Nowadays, huge clusters of GPUs are used to train neural network models to support features such as LLMs and Generative AI. But a few know that the Computer Graphics and Gaming industry had a huge role in pushing the advancement of GPUs to its modern state.

The development of GPU was inspired by the advent of gaming consoles such as the original Play Station and Sega Saturn which supported high quality 3D games. These consoles developed in the early 1990s supported remarkable quality of real time 3D graphics for the time since the concept of GPUs did not exist and the hardware available was extremely limited. This inspired many people to work towards building hardware that could accelerate graphics processing on a PC in a similar manner.

{{< figure src="images/image-07.jpg" caption="The conventional graphics pipeline used in modern applications." >}}

The early GPUs such as the NVIDIA GeForce 256 consisted of a graphics pipeline that was hardwired on the graphics card, meaning that the graphics pipeline cannot be modified and used for purposes other than graphics processing and rendering. In these early GPUs, even the shaders were parameterized programs on the GPU which could controlled by developers who would supply parameters to acquire the desired result, however developers were unable to modify the underlying shaders to control the data once it is passed to the GPUs.

However as PC games started to become more sophisticated, the requirement of offloading certain graphics processing to the GPU became essential, which was not possible in the earlier GPUs since the shaders programs were fixed. Hence, GPUs such as NVIDIA GeForce 3 (NV 20) and GeForce FX introduced programmable vertex and fragment shaders which enabled custom and sophisticated data manipulation of graphics data on the GPU.

As the years progressed, the GPUs increased the computing capabilities of these cards to support the ever increasing needs of the gaming industry which pushed for more sophisticated graphics rendering techniques in their games. Overtime, these graphics cards started being used even in consoles. The PlayStation 3 console which used the NVIDIA Curie CPU chip and a RSX GPU chip that was close to NVIDIA G70 architecture supported some games like Crysis 3 which had astonishing graphics for the time.

{{< figure src="images/image-08.jpg" caption="Real-time gameplay of Crysis 3" >}}

However, this increase in computing capability caught the eye of some scientific folks who started to harness the computing power to perform intensive calculations for several crucial scientific applications. In 2010, the Condor cluster was built as a supercomputer by the US Air Force which consisted of 1,760 PS3 consoles connected in a network to get a throughput of whopping 500 trillion FLOPS or 500 TFLOPS!

However, since the GPUs had a hardwired graphics pipeline, scientists had to transform their algorithms into inscrutable shader code to get it to execute on a GPU. This severely limited their ability to extract the output of the computation in a standard and sensible format as they were forced to extract the results and transform it into a visual format.

As a solution to this problem, NVIDIA as a pioneering GPU manufacturer started implementing a streaming programming model into their GPUs which allowed the streaming multiprocessors (which can be thought of as a GPU computing core) on the GPUs to be programmed by developers instead of only being used in the graphics pipeline. This allowed the GPUs to be utilized for scientific applications. NVIDIA introduced the CUDA programming language to enable developers to build custom applications to utilize the parallel computing capability of an NVIDIA GPU.

Since the GPUs provided a high number of FLOPS (FLoating point Operations Per Second), they proved to be a game-changer in the advancement of Deep Learning. The development of models such as AlexNet and ResNet drew the attention of developers all around the world, which resulted in traditional techniques becoming obsolete. High availability of these programmable GPUs enabled the large-scale and exponential development of algorithms and tools in the field of Deep Learning models. The LLMs and Generative AI models we use nowadays are often trained on clusters often containing more than 1000 GPUs!

### Concluding Thoughts

In retrospect, it is amazing to see how an initiative stated by a few academicians in the early 1960s transformed the way we perceive information, entertainment, and the way we now live our lives. It is easy to take the advanced graphics we see nowadays for granted as it is found in all common digital interactions, but I strongly feel that it highlights the important transformations which can be brought into the world with a coordinated and well organized collaboration of academicians and industry engineers!

### Bibliography

 **CG research at OSU** — <https://www.computer.org/csdl/magazine/cg/2021/03/09425388/1tpx2XaOQqQ>

**OpenGL and WebGL** — <http://learnwebgl.brown37.net/the_big_picture/webgl_history.html>

**NVIDIA GPUs** — <https://www.nvidia.com/content/nvision2008/tech_presentations/technology_keynotes/nvision08-tech_keynote-gpu.pdf>

**Prominent Events in CG** — <https://technofaq.org/posts/2017/11/evolution-of-computer-graphics/>

**Textures and Reflection in Computer Generated Images** — <https://papers.cumincad.org/data/works/att/186e.content.pdf>

**The Reyes Image Rendering Architecture** — <https://graphics.pixar.com/library/Reyes/paper.pdf>

**Silicon Graphics** — <https://en.wikipedia.org/wiki/Silicon_Graphics>

**PHIGS** — <https://en.wikipedia.org/wiki/PHIGS>

**OpenGL** — <https://learnwebgl.brown37.net/the_big_picture/webgl_history.html>

**Evolution of GPUs** — <https://ieeexplore.ieee.org/document/9623445>

**The Condor Cluster** — <https://phys.org/news/2010-12-air-playstation-3s-supercomputer.html>

**The RSX GPU in PS3** — <https://en.wikipedia.org/wiki/RSX_Reality_Synthesizer>
