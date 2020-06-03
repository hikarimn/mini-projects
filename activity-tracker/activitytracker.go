package activitytracker

import (
	"encoding/json"
	"errors"
	"io"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"strings"
	"time"
)

/*
Define API response field
*/

//ActivityTracker field
type ActivityTracker struct {
	SERVICE_KEY string
}

//Reason field
type Reason struct {
	ReasonCode int `json:"reasonCode,omitempty"`
}

//Credential field
type Credential struct {
	Type string `json:"type,omitempty"`
}

//Host field
type Host struct {
	Address string `json:"address,omitempty"`
	Agent   string `json:"agent,omitempty"`
}

/*
Define API response objects (compose of the above fields)
*/

//Target object
type Target struct {
	ID      string `json:"id,omitempty"`
	TypeURI string `json:"typeUri,omitempty"`
	Name    string `json:"name,omitempty"`
	Host    Host   `json:"host"`
}

//Initiator object
type Initiator struct {
	Name       string     `json:"name,omitempty"`
	ID         string     `json:"id,omitempty"`
	TypeURI    string     `json:"typeUri,omitempty"`
	Host       Host       `json:"host"`
	Credential Credential `json:"credential"`
}

//Event object
type Event struct {
	Account         string    `json:"_account"`
	Cluster         string    `json:"_cluster"`
	Env             string    `json:"_env"`
	Host            string    `json:"_host"`
	Ingester        string    `json:"_ingester"`
	Logtype         string    `json:"_logtype"`
	File            string    `json:"_file"`
	Line            string    `json:"_line"`
	Ts              int       `json:"_ts"`
	Platform        string    `json:"_platform"`
	App             string    `json:"_app"`
	IP              string    `json:"_ip"`
	Key             string    `json:"__key"`
	Bid             string    `json:"_bid"`
	Action          string    `json:"action"`
	Outcome         string    `json:"outcome"`
	Message         string    `json:"message"`
	Severity        string    `json:"severity"`
	EventTime       string    `json:"eventTime"`
	EventType       string    `json:"eventType"`
	TypeURI         string    `json:"typeURI"`
	ID              string    `json:"id"`
	RequestData     string    `json:"requestData"`
	ResponseData    string    `json:"responseData"`
	SaveServiceCopy bool      `json:"saveServiceCopy"`
	LogSourceCRN    string    `json:"logSourceCRN"`
	ID2             string    `json:"_id"`
	Initiator       Initiator `json:"initiator"`
	Target          Target    `json:"target"`
	Reason          Reason    `json:"reason"`
}

//Events object
type Events struct {
	EventItem []Event
}

//AddEvent appends an event to events and does API request
func (events *Events) AddEvent(eventItem Event) []Event {
	events.EventItem = append(events.EventItem, eventItem)
	return events.EventItem
}

//makeAPIRequest takes url and service key
func makeAPIRequest(url string, key string) ([]byte, error) {
	// Build an http client and control timeout
	client := &http.Client{
		Timeout: time.Second * 10,
	}

	// Make a new GET request
	req, reqErr := http.NewRequest("GET", url, nil)
	if reqErr != nil {
		log.Fatal("Error with making a new request: \n", reqErr)
		return nil, reqErr
	}

	// Authentificate with a service key
	req.SetBasicAuth(key, "")

	// Request and get a response
	resp, getErr := client.Do(req)
	if getErr != nil {
		log.Fatal("Error with getting a response: \n", getErr)
		return nil, getErr
	}
	log.Printf("resp.statuscode = : %d", resp.StatusCode)

	// defer the closing of the response body
	defer resp.Body.Close()

	// read the http response body into a byte stream
	bodyBytes, readErr := ioutil.ReadAll(resp.Body)
	if readErr != nil {
		log.Fatal("Error with reading a response: \n", readErr)
		return nil, readErr
	}

	log.Printf("request sent")
	return bodyBytes, nil
}

//GetEventsToNow returns an Event object made within past n seconds
func (at *ActivityTracker) GetEventsToNow(nseconds int) (*Events, error) {
	var evts Events
	// if no API key presents, return error
	if at.SERVICE_KEY == "" {
		return nil, errors.New("No API keys present")
	}

	key := at.SERVICE_KEY
	to := int(time.Now().Unix())
	from := to - nseconds

	// concatenate url to pass
	urlbase := "https://api.eu-de.logging.cloud.ibm.com/v1/"
	query := "export?to=" + strconv.Itoa(to) + "from=" + strconv.Itoa(from)
	url := urlbase + query

	// request!
	bodyBytes, reqErr := makeAPIRequest(url, key)
	if reqErr != nil {
		log.Fatal("Error with makeAPIRequest func: \n", reqErr)
		return nil, reqErr
	}

	//The input is a set of independent json obejcts, hence
	//iterate over them with Decoder and append each event to events slices
	bodyStr := string(bodyBytes)
	dec := json.NewDecoder(strings.NewReader(bodyStr))
	for {
		var evt Event
		if dcdeErr := dec.Decode(&evt); dcdeErr == io.EOF {
			break
		} else if dcdeErr != nil {
			log.Fatal("Error with Decoder : \n", dcdeErr)
		}
		evts.AddEvent(evt)
	}

	return &evts, nil
}
