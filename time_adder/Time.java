public class Time{
    private long hour;
    private long minute;
    private String meridiem;

    private long minutesOriginal;
    private long minutesChanged;

    public static int hourIdx = 0;
    public static int minuteIdx = 1;
    public static int meridiemIdx = 2;

    public String AddMinutes(String timeString, long minutes){
        minutesOriginal = stringToMinutes(timeString);
        minutesChanged = addMinutes(minutesOriginal, minutes);
        return(minutesToString(minutesChanged));
    }

    private long addMinutes(long minutesOriginal, long minutesAdded){
        return(minutesOriginal + minutesAdded % 1440);
    }

    private long stringToMinutes(String timeString){
        String[] terms = timeString.split("[\\s,:]+");

        if(!(validateString(terms))){
            throw new IllegalArgumentException("Your time must be in this format '[H]H:MM {AM|PM}'");
        }

        hour = (Long.parseLong(terms[hourIdx]) == 12) ? 0 : Long.parseLong(terms[hourIdx]);
        minute = Long.parseLong(terms[minuteIdx]);
        meridiem = terms[meridiemIdx];

        return((meridiem.equals("AM")) ? (hour*60+minute) : ((hour+12)*60+minute));
    }

    private String minutesToString(long minutesLong){
        minutesLong = minutesLong % 1440;
        minutesLong = ((minutesLong < 0) ? 1440 + minutesLong : minutesLong);

        hour = minutesLong / 60;
        minute = minutesLong % 60;
        meridiem = ((hour >= 12) ? "PM" : "AM");

        hour = ((hour > 12 ) ? hour - 12 : hour);
        hour = ((hour == 0) ? 12 : hour);

        String result = (Long.toString(minute).length() == 1 ? 
            concat(Long.toString(hour), ":0", Long.toString(minute), " ", meridiem):
            concat(Long.toString(hour), ":", Long.toString(minute), " ", meridiem));
        return(result);
    }
    
    private boolean validateString(String[] terms){
        if (terms == null || terms.length == 0){
            return(false);
        }        
        return(validateStringLength(terms) && validateHour(terms[hourIdx]) && validateMinute(terms[minuteIdx]) && validateMeridiem(terms[meridiemIdx]));
    }

    private boolean validateStringLength(String[] timeStringArr){
        return(timeStringArr.length==3);
    }

    private boolean validateHour(String hourString){
        return((0 < Integer.parseInt(hourString)) && (Integer.parseInt(hourString) <= 12));
    }

    private boolean validateMinute(String minuteString){
        return((0 <= Integer.parseInt(minuteString)) && (Integer.parseInt(minuteString) < 60));
    }

    private boolean validateMeridiem(String meridiemString){
        return((meridiemString.equals("AM")) || (meridiemString.equals("PM")));
    }

    private String concat(String s1, String s2, String s3, String s4, String s5){
        StringBuffer sb = new StringBuffer();
        sb.append(s1);
        sb.append(s2);
        sb.append(s3);
        sb.append(s4);
        sb.append(s5);
        return sb.toString();
    }
}
