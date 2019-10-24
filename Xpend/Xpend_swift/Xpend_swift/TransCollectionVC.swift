//
//  TransCollectionVC.swift
//  Xpend_swift
//
//  Created by IOSLevel-01 on 24/10/19.
//  Copyright © 2019 sjbit. All rights reserved.
//

import UIKit

class TransCollectionVC: UICollectionView {

    /*
    // Only override draw() if you perform custom drawing.
    // An empty implementation adversely affects performance during animation.
    override func draw(_ rect: CGRect) {
        // Drawing code
    }
    */
    
    override var contentSize:CGSize {
        didSet {
            self.invalidateIntrinsicContentSize()
        }
    }
    
    override var intrinsicContentSize: CGSize {
        self.layoutIfNeeded()
        return CGSize(width: UIView.noIntrinsicMetric, height: contentSize.height)
    }
    
}
