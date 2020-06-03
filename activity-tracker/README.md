A wrapper for the IBM Cloud Activity Tracker with LogDNA API Service for an use in Golang.
For information about the API and how to get a 32 characters service key, please see [this](https://cloud.ibm.com/docs/services/Log-Analysis-with-LogDNA?topic=LogDNA-export#api).

### Prerequisites

```shell
$ export SERVICE_KEY="your service key"
```

### Installing

```shell
$ go get github.com/hikarimn/activity-tracker
```

### Usage

```go
package main

import "github.com/hikarimn/activity-tracker"

func main(){
	at := activitytracker.ActivityTracker{SERVICE_KEY: os.Getenv("SERVICE_KEY")}

	var events *activitytracker.Events
	var err error

	// Getting events made within past 24*60*60 seconds (24hrs) to now
	events, err = at.GetEventsToNow(24*60*60)
	if err != nil {
	log.Fatal(err)
	}	

	// Getting access to the latest event
	s := events.EventItem[0].Message
	i := events.EventItem[0].Initiator.Name
	log.Printf("Getting access to the latest event")
	log.Printf("%s initiated by %s\n", s, i)
}
```
this returns something like this
```shell
2019/08/07 11:03:50 resp.statuscode = : 200
2019/08/07 11:03:50 request sent
2019/08/07 11:03:50 Getting access to the latest event
2019/08/07 11:03:50 IAM Identity Service: login user-refreshtoken someone@email.com initiated by someone@email.com

```
