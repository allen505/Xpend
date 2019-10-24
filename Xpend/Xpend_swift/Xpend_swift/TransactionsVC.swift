//
//  TransactionsVC.swift
//  Xpend_swift
//
//  Created by IOSLevel-01 on 24/10/19.
//  Copyright © 2019 sjbit. All rights reserved.
//

import UIKit

class TransactionsVC: UIViewController,UICollectionViewDataSource,UICollectionViewDelegate {
    
    var testDates=["01-Jul","02-Sep","04-Sep","02-Nov"]
    var testTags=["Food","Clothing","Food","Furniture"]
    var testDesc=["Happy Chopsticks","Gucci","Happy Chopsticks","Pakad Mane"]
    var testCosts=["30","40","10","50"]
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        return testTags.count
    }
    
    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "indiCell", for: indexPath) as! IndividualTransaction
        cell.date.text=testTags[indexPath.row]
        cell.cost.text="$ "+testCosts[indexPath.row]
        cell.desc.text=testDesc[indexPath.row]
        
        return cell
    }
    

    override func viewDidLoad() {
        super.viewDidLoad()


        // Do any additional setup after loading the view.
    }
    

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
