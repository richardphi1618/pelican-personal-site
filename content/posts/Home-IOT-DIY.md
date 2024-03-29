Title: DIY Home IoT Network
date: 2020-04-22
tags: IoT
category: home projects
author: Richard Blanchette
summary: Write up of how I was able to create a local IoT network in my home.
##############

I want my first post to be a top-level view of how I laid my house out for collecting and dashboarding data. Let us start with the diagram below:

![Home-Network]({static}/images/iot-diy/HomeMQTTNetwork.jpg)

Whoa…. Lots going on here.

Let us break it down starting from the “load” or sensor/panels. I collect data from multiple different sensor suites, and toggle bits through different interfaces, but they all share one thing in common - they are either subscribers or publishers to my MQTT broker. For more on MQTT check out this article: [What is MQTT and How It Works.](https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/) In short, the broker acts as the middle man / traffic cop on what the data is and where this data should go. There are different ways to setup a Broker, but for my setup I simply had it collect and distribute the data and then delete it when it was done. No need to store it there when a database can do that for me.

![mqtt-broker](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2017/01/mqtt_broker.png?resize=750%2C303&ssl=1)

My next problem, I needed a place for my broker to reside as a server. For full control, I decided to setup my own broker in my house. Other setups use off-site brokers and that is what is typical for “cloud” based solutions, but that can be costly. I also knew I wanted to log my data to a database, that would require some post/pre-processing before I logged, and I needed a way to show or “dashboard” this data over time. So, I went with what I thought would be the cheapest (let’s be honest - the most fun) option and built a home server myself out of new and old spare computer parts I had lying around.

![Home Server]({static}/images/iot-diy/homeserver.jpg)

I also knew that having all of these service running on a single machine could become cumbersome and often times would be messy as you could potentially have the services over lap. I was doing some research on docker at the time and wanted to learn more so this seemed like a good time. What a great tool! Docker is awesome! Not only docker itself but the rabbit hole of other services and management tools out there that go with it. For some great examples look at: [Image list](https://fleet.linuxserver.io) developed by [LinuxServer.io](https://www.linuxserver.io) For now I'll gloss over it but would like to spend more time on documenting how my docker is setup. In summary I have multiple "containers" running each of these services as a complete "stack" or solution. Portainer is a seperate container I use to manage and review the health and settings of each of the containers without having to rely on the command line.

![Portainer]({static}/images/iot-diy/portainer.png)

Okay, so now that I have my environment and I have my communication from my devices to my server and it’s all talking over my home network (the easy part -ha). I needed to log the data somewhere. I didn’t want to point the data, being collected through the broker, straight into a database. Even if I did my best trying to maintain uniformity, there are things that just come across differently from different devices. Therefore, I needed some way of massaging the data and cleaning it before I stored it in my database. I stumbled across Node-Red as a powerful IO and data tool from my work in the industrial field. Advantech has some really fascinating products coming out using this.

Node-Red is a graphic way of writing java code. I knew nothing about java going into this but was able to get a very basic program up and running in about an hour or two. What blew me away was the ability to download everything you needed for a dashboard from within the browser-based development environment. The layout also reminded me a lot of what I would see in the IEC-61131 languages known as function blocks. I didn’t need the code behind the block but the read-me associated with the block would tell me everything I needed to know about how to use it. Node-red is Java and I can see how people love it and hate it. The biggest thing I had to get used to was its’ event driven nature versus what I am traditionally used to with cyclic programming. Sample of what some of my code looks like:

![Node-Red Flow]({static}/images/iot-diy/node-red.png)

Right, now that I have my data cleaned and polished and ready for a database, I need to pick a database…. There are soooo many! The most ubiquitous database structure out there that I’ve seen/used was SQL (and the dozen or so cousins/forks from). The problem I saw with using SQL is that the data I wanted to record needed to be recorded with a time stamp. All the SQL based databases are relational, meaning I would have to do an extra step in managing large amounts of continuous data. InfluxDB on the other hand seemed to take all data acquired and automatically assigned it with a time stamp. It seemed better built for how I wanted to see my data, which is important for my dashboard.

Dashboard is the most exciting part. I am not only seeing the state of my data, but I can make inferences based on what my data is doing over time. So many “AHA!” moments happen when you start doing this. Grafana seemed to be a top choice for a lot of people in the IT industry and it seemed light weight, and gorgeous! If you ever have time and want to go down a rabbit hole just google Grafana graphs and the data science nerd in me just can’t stop staring. Once I had Grafana up and running, it was less than an hour to point Grafana to my database and then it was simple to add scaling and titles, and viola! You too can make your data beautiful.

![Grafana Dashboard]({static}/images/iot-diy/grafana.png)

So, from the picture above, you’ll see I’m also playing around seeing if I can monitor workload/ memory usage of the remote devices as well as my server (needs some work). Overall I am very happy with how it turned out. I also was able to add local weather with a node-red module that I found (in green).

For now, I’m going to leave the post here. This intended to be a high-level look. Apologies if there is anything you were looking for more detail on. Feel free to reach out and I will happily give guidance or point you in the right direction if you have any questions. I may pick one or two pieces here to develop more into a how-to guide.

Overall, I am extremely happy with this setup. The biggest thing I wanted to focus on here was flexibility and modular-iblity (not a word, but my blog so deal). What I didn’t go into here was how I use this same setup to control my lights and devices in my house either directly or with the use of IFTTT. Somebody built a Node-Red module that allows you to communicate directly with a Phillips Hue Hub. I have some Wyze plugs as well that I am not able to talk directly to on my network, but I was able to setup an IFTTT service using webhooks. Docker is such a rabbit hole for more projects, and I am looking forward to diving further in. Docker-compose, which I did not cover above, has also been a huge help. It   gives basic instructions on what I built and how I built it so I can come back to something I did months ago and immediately know how it is configured and setup.

I started this with basic server grade programming knowledge and about 5 years of experience programming machines. I wanted to get experience developing a solution from a sensor all the way to a server-based solution trying to bridge the gap. I see a lot of IoT potential in the near future but ultimately, I found there are many parts to build this complete picture well. Reach out if you think I did something well or if you think I did something wrong. For now, this is the foundation I hope to build many other things on top of.

\*\*\*Follow Up:  
Recently Did a presentation on this in more detail. See my PowerPoint slides here: [Home Industrial Network Presentation](https://1drv.ms/p/s!AnRPoczwFXt-gZlFK6aLPQ_aAGvAcQ?e=w1e1Ch)

\*\*\*Here is an embedded iframe of the final product:

<iframe id="inlineFrameExample"
    title="Inline Frame Example"
    width=100%
    height="800"
    src="https://graf.richardphi.dev/d/jorQjxQWk/home?orgId=1&amp;refresh=5s&amp;amp">
</iframe>