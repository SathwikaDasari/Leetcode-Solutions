class Solution {
    public List<List<Integer>> mergeSimilarItems(int[][] items1, int[][] items2) {
        List<List<Integer>> list = new ArrayList<>();
        
        for(int[] element : items1) {
            int val = element[0];
            int weight = element[1];
            list.add(new ArrayList<>(Arrays.asList(val, weight)));
        }

        for(int[] element : items2) {
            int val = element[0];
            int weight = element[1];
            boolean flag = false;

            for(List<Integer> l : list) {
                if(l.get(0).equals(val)) {
                    l.set(1, l.get(1) + weight);
                    flag = true;
                    break;
                }
            }

            if(!flag) {
                list.add(new ArrayList<>(Arrays.asList(val, weight)));
            }
        }

        Collections.sort(list, 
            new Comparator<List<Integer>>() {
                public int compare(List<Integer> l1, List<Integer> l2) {
                    return l1.get(0) - l2.get(0);
                }
            }
        );
        return list;
    }
}