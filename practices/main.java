/*

The goal of this exercise is to iterate over the elements of the provided iterator object that contains multiple transactions for multiple users. Once you have seen all of the transactions for a given user, you should immediately call processUserBatchTransactions(.., ...), and then proceed to the next user.
  
 The Iterator<Transaction> object contains entries that look like the below. The length of the Iterator is unknown but returns an entry one at a time in order of a user. For example, you will receive: trans1_for_user1, trans2_for_user1, trans1_for_user2, trans1_for_user3, and you will call processUserBatchTranscations 3 times.
 
 Example entries:
 
    {
      id: 1,
      amount: 5030,
      user_balance: 6000,
      bank_user_id: 'user_id_1',
      bank_name: ‘chase’,
      timestamp: 1534871319,
      vendor_name: “McDonalds”
    },
    {
      id: 1,
      amount: 5030,
      user_balance: 6000,
      bank_user_id: 'user_id_1',
      bank_name: ‘chase’,
      timestamp: 1534871319,
      vendor_name: “McDonalds”
    },
    {
      id: 2,
      amount: 4000,
      user_balance: 5000,
      bank_user_id: 'user_id_1',
      bank_name: ‘chase’,
      timestamp: 1534871349,
      vendor_name: “Burger King”
    },
    {
      id: 3,
      amount: 8030,
      user_balance: 4000,
      bank_user_id: 'user_id_2',
      bank_name: ‘chase’,
      timestamp: 1534871399,
      vendor_name: “Kentucky Fried Chicken”
    }
 
   We'd like a final solution which is reasonably memory and time efficient.
   
*/

 
class Scratch {

    public int processAllTransactions(Iterator<Transaction> allTransactions) {
      // TODO: fill this method in to iterate over the elements of this iterator and once you have recieved all the entries for a given user call the function belo
        ArrayList<Transaction> transForCurrUser = new ArrayList<>(); 
        Transaction nextTrans = allTransactions.next();
        String currUserId = nextTrans.userId();
        transForCurrUser.add(nextTrans);
        
        while(allTransactions.hasNext()){
            Transaction nextTrans = allTransactions.next();
            String userId = nextTrans.userId();
            if (currUserId == userId){
                transForCurrUser.add(nextTrans);
            } else {
                processUserBatchTransactions(userId, transForCurrUser);
                currUserId = userId;
                transForCurrUser = new ArrayList<>(); 
                transForCurrUser.add(nextTrans);
            }

        }
        processUserBatchTransactions(userId, transForCurrUser);
        
 
    }
    
  
    /**
     * CALL THIS METHOD ONCE PER USER - you can assume it takes O(1)
     * This method processes all of the transactions related to a single user
     * @param userId the ID of the user whose transactions are being passed in
     * @param transactions a list of transactions only belonging to that user
     * @throws IllegalArgumentException if the transactions passed in do not ALL belong to userId
     */
    public abstract void processUserBatchTransactions(String userId, List<Transaction> transactions);
}
