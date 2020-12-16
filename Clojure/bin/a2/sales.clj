;******************************************************************************
;Assignment2-Clojure
;Dhruvi Gadhiya
;40084176
;*******************************************************************************
(ns a2.sales)
(require '[clojure.string :as str])

(defn Read []
  (def string1 (slurp "cust.txt"))
  (def string2 (str/split-lines (str/replace string1 #"\|" ",")))
  (def string3 (map #(str/replace-first % #"," "|") string2))
  (def string4 (map #(str/split % #"[|]") string3))
  (def cust (apply merge (map #(sorted-map (first %) (rest %)) string4)))
  
  (def string11 (slurp "prod.txt"))
  (def string12 (str/split-lines (str/replace string11 #"\|" ",")))
  (def string13 (map #(str/replace-first % #"," "|") string12))
  (def string14 (map #(str/split % #"[|]") string13))
  (def prod (apply merge (map #(sorted-map (first %) (rest %)) string14)))
  
  (def string21 (slurp "sales.txt"))
  (def string22 (str/split-lines (str/replace string21 #"\|" ",")))
  (def string23 (map #(str/replace-first % #"," "|") string22))
  (def string24 (map #(str/split % #"[|]") string23))
  (def sale (apply merge (map #(sorted-map (first %) (rest %)) string24)))


  (def keysofsale (sort-by first (keys sale)))
  ;all values of sales
  (def y (map #(str/split (str/join ", " (get sale %)) #",") (sort-by first (keys sale))))
  ;only customer id from sales
  (def custidinsale(map #(first %) y))
  ;(println custidinsale)
  ;only prod id from sales
  (def prodidinsale(map #(nth % 1) y))
  ;(println prodidinsale)
  ;all value of customers from sales custid
  (def x (map #(str/split (str/join ", " (get cust %)) #",") custidinsale))
  ;onlu name of cust from sales custid
  (def custnameinsale(map #(first %) x))
  ;(println custnameinsale)
  ;all value of prod from sales prodid
  (def xx (map #(str/split (str/join ", " (get prod %)) #",") prodidinsale))
  (def prodnameinsale(map #(first %) xx))
  ;(println prodnameinsale)
  (def noofsale(map #(nth % 2) y)) ;last col of sale
  (def len (count sale))
  
  ;all values of product
  (def p (map #(str/split (str/join ", " (get prod %)) #",") (sort-by first (keys prod))))
  ;keys of prod
  (def keysofprod (sort-by first (keys prod)))
  ;name of prod
  (def nameofprod (map #(first %) p))
  ;(println nameofprod)
  ;price of prod
  (def priceofprod (map #(nth % 1) p))
  ;(println priceofprod)
  )
(Read)

(def Menu [])
(defn PrintCust []
  (def cust1 (apply merge (map #(sorted-map (Integer/parseInt(first %)) (rest %)) string4)))
  (doall (map #(println %":["(get cust1 %)"]") (sort (keys cust1))))
  (Menu))

(defn PrintProd []
  (def prod1 (apply merge (map #(sorted-map (Integer/parseInt(first %)) (rest %)) string14)))
  (doall (map #(println %":["(get prod1 %)"]") (sort (keys prod1))))
  (Menu))

(defn PrintSales []
  (def len (count sale))
  (loop [a 0]
      (if (< a len) 
        (do 
          (println (nth keysofsale a)":[\""(nth custnameinsale a)"\"\""(nth prodnameinsale a)"\"\""(nth noofsale a)"\"]")
          (recur (inc a)))))
  (Menu))

(defn TotalSales [custname]
  (def y (map #(str/split (str/join ", " (get cust %)) #",") (sort-by first (keys cust))))
  (def custnames(map #(first %) y))
  (def keysofcust (sort-by first (keys cust)))
  (def len (count cust))
  (loop [a 0]
      (if (< a len) 
        (do
          (def x1 (nth custnames a))
          (def x2 custname)
          (if (= x1 x2) 
            (def custid (nth keysofcust a)))
          (recur (inc a)))))
  (def total 0.0)
  (def len (count sale))
  (loop [a 0]
    (if (< a len)
      (do
        (if (= (nth custidinsale a) custid) 
          (do
            (def prodid (Integer. (nth prodidinsale a)))
            (def price (Double. (nth priceofprod (- prodid 1))))
            (def itembuy (Double. (nth noofsale a)))
            (def total (+ total (* itembuy price)))
            ))
        (recur (inc a)))))
  (println custname": "total)
  (Menu))

(defn TotalCount [prodname]
  (def prodlen (count prod))
  (loop [a 0]
      (if (< a prodlen) 
        (do 
          (def x1 (nth nameofprod a))
          (def x2 prodname)
          (if (= x1 x2) 
            (def prodid (nth keysofprod a)))
          (recur (inc a)))))
  ;(println prodid)
  (def totalsale 0)
  (def len (count sale))
  (loop [a 0]
      (if (< a len) 
        (do 
          (if (= prodid (nth prodidinsale a)) (def totalsale (+ totalsale (Integer. (nth noofsale a)))))
          (recur (inc a)))))
  (println prodname": "totalsale)
  (Menu))

(defn Exit [] 
  (System/exit 0))

(defn Menu []
	(println "***Sales Menu***")
	(println "----------------------")
	(println "1. Display Customer Table")
	(println "2. Display Product Table")
	(println "3. Display Sales Table")
	(println "4. Total Sales For Customer")
	(println "5. Total Count For Product")
	(println "6. Exit")
	(println "Enter an Option :")
	(def option (read-line))
	
	(case option
	  "1" (PrintCust)
	  "2" (PrintProd)
	  "3" (PrintSales)
	  "4" (do (println "Enter customer name :")(def custname (read-line)) (TotalSales custname))
	  "5" (do (println "Enter product name :")(def prodname (read-line)) (TotalCount prodname))
	  "6" (Exit)
   (Menu)))

(Menu)

