class TimeMap {

    private record Entry(int timestamp, String value){}

    private final Map<String, List<Entry>> store;

    public TimeMap() {
        store=new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        store.computeIfAbsent(key,k->new ArrayList<>()).add(new Entry(timestamp,value));//???
    }
    
    public String get(String key, int timestamp) {
        List<Entry> arr=store.getOrDefault(key,Collections.emptyList());
        int l=0;
        int r=arr.size()-1;
        String ans="";
        while(l<=r){
            int mid=(l+r)/2;
            if (arr.get(mid).timestamp()<=timestamp){
                ans=arr.get(mid).value();
                l=mid+1;
            }else{
                r=mid-1;
            }
        }
        return ans;
        
    }
}
