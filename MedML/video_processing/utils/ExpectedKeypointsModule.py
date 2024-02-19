import numpy as np

class ExpectedKeypoints:
    def __init__(self) -> None:

        self.expected_keypoints = {
            'downward_dog' : np.array([
                [0.5718105, 0.66141796, 0.54200286],
                [0.50217485, 0.71327007, 0.7266921],
                [0.5071678, 0.5930058, 0.6886661],
                [0.5270589, 0.7783836, 0.63765943],
                [0.5395051, 0.50478303, 0.5802833],
                [0.81126285, 0.9333791, 0.36040258],
                [0.7707097, 0.34096187, 0.7861225],
                [0.9649166, 0.96254253, 0.05885383],
                [0.93376565, 0.29798463, 0.01498279],
                [0.8012082, 0.86318886, 0.01377812],
                [0.50790673, 0.48212466, 0.04807808],
                [1.0284973, 0.90336245, 0.00782078],
                [0.46554837, 0.48701307, 0.0140808],
                [0.8494258, 0.97905815, 0.0168888],
                [0.7919068, 0.32009828, 0.03491595],
                [0.7552506, 1.0047088, 0.00591631],
                [0.712418, 0.5613036, 0.00223848]
            ]),

            'cobra' : np.array([
                [0.35584372, 0.7513099 , 0.5054945 ],
                [0.34154892, 0.7401547 , 0.6909735 ],
                [0.3415668  ,0.7440542,  0.7003814 ],
                [0.35509354 ,0.6983301 , 0.5968837 ],
                [0.3578204  ,0.7005153 , 0.7398889 ],
                [0.44468552 ,0.67906606 ,0.79406613],
                [0.4550224  ,0.6825337 , 0.65016955],
                [0.58883995 ,0.67452896 ,0.47643593],
                [0.6148588  ,0.6835231,  0.5545329 ],
                [0.68111444 ,0.71922123 ,0.43152288],
                [0.69180554 ,0.72255296 ,0.61084497],
                [0.6498467  ,0.5623442 , 0.6525018 ],
                [0.6655383  ,0.57790667 ,0.5889535 ],
                [0.6758326   ,0.40153202 ,0.41661975],
                [0.68300045 ,0.39241618 ,0.4996618 ],
                [0.676959   ,0.21567714 ,0.5482763 ],
                [0.681631   ,0.21253753 ,0.57772744]
            ]),

            'tree_pose' : np.array([
                [0.23007223, 0.39760622, 0.41683072],
                [0.22295943, 0.41038176, 0.67800856],
                [0.22206008, 0.3898575 , 0.6452982 ],
                [0.23161727, 0.42774963, 0.67280424],
                [0.23123094, 0.37366807, 0.5778757 ],
                [0.29216903, 0.45771572, 0.67516464],
                [0.29209352, 0.3378952 , 0.6632625 ],
                [0.3833315 , 0.49083072, 0.35793918],
                [0.37762696, 0.27997965, 0.4025226 ],
                [0.3784166 , 0.46779358, 0.29223746],
                [0.37276492, 0.31678763, 0.13555199],
                [0.49146944, 0.43118387, 0.58965445],
                [0.48795462, 0.3691834 , 0.67668337],
                [0.6439178 , 0.40199614, 0.5626835 ],
                [0.6219053 , 0.39344728, 0.20896354],
                [0.6711244 , 0.39700863, 0.30009195],
                [0.66049874, 0.4000659 , 0.31522733]
            ]),

            'chair_pose' : np.array([
                [0.36121926 ,0.39623404 ,0.45834774],
                [0.34959114 ,0.40469715 ,0.37878007],
                [0.35130033 ,0.38820726 ,0.58635205],
                [0.35643047 ,0.42916626 ,0.5576739 ],
                [0.3552925  ,0.39115795 ,0.44215053],
                [0.4075685  ,0.44662058 ,0.4594301 ],
                [0.40739518 ,0.37019318 ,0.51525366],
                [0.41803357 ,0.41169512 ,0.14166465],
                [0.41139376 ,0.2728561  ,0.48355758],
                [0.4025833  ,0.40214965 ,0.19040246],
                [0.39306244 ,0.17995858 ,0.4710712 ],
                [0.57939065 ,0.47825179 ,0.6068841 ],
                [0.5767667  ,0.42440313 ,0.59366834],
                [0.6287154  ,0.40180397 ,0.3045406 ],
                [0.60412496 ,0.30881083 ,0.64104307],
                [0.7491471  ,0.43701524 ,0.47410607],
                [0.7428312  ,0.38297397 ,0.50466484]
            ]),

            'shoulder_stand' : np.array([  
                [0.7327523  ,0.515426   ,0.30620062],
                [0.74286544 ,0.5271431  ,0.43422928],
                [0.7375676  ,0.5255794  ,0.4194957 ],
                [0.7713883  ,0.52462566 ,0.5405327 ],
                [0.76266396 ,0.5176771  ,0.43837526],
                [0.7645836  ,0.46025604 ,0.4757743 ],
                [0.7576834  ,0.4433655  ,0.60886025],
                [0.81224364 ,0.3466667  ,0.10363124],
                [0.8483965  ,0.30191088 ,0.4407038 ],
                [0.76312757 ,0.38950622 ,0.12192098],
                [0.84005034 ,0.32737875 ,0.13117792],
                [0.57484025 ,0.43234843 ,0.42212254],
                [0.5671292  ,0.44671115 ,0.51541287],
                [0.3562711  ,0.46280846 ,0.42557958],
                [0.35753125 ,0.46153304 ,0.41824734],
                [0.16060269 ,0.4599607  ,0.4451373 ],
                [0.1550943  ,0.4658326  ,0.47436288]
            ]),

            'warrior_pose' : np.array([
                [0.29872388 ,0.33334193 ,0.4935175 ],
                [0.28767878 ,0.34500498 ,0.7057759 ],
                [0.28847194 ,0.32682702 ,0.5326239 ],
                [0.29391718 ,0.36805385 ,0.69398314],
                [0.29779822 ,0.31792656 ,0.73875433],
                [0.35544643 ,0.40678355 ,0.6921601 ],
                [0.36534977 ,0.28226385 ,0.7843596 ],
                [0.38901016 ,0.48308367 ,0.47164276],
                [0.3685866  ,0.19136766 ,0.5642954 ],
                [0.3959639  ,0.5772604  ,0.4641576 ],
                [0.34531975 ,0.07812722 ,0.56249475],
                [0.5505445  ,0.40683472 ,0.738961  ],
                [0.5514799  ,0.3297712  ,0.77879024],
                [0.6462457  ,0.4851644  ,0.4185223 ],
                [0.5956495  ,0.20347884 ,0.82893246],
                [0.7264732  ,0.55527604 ,0.58103466],
                [0.75409055 ,0.1896907  ,0.78533643]
            ]),

            'triangle_pose' : np.array([
                [0.53693855 ,0.25501654 ,0.36709106],
                [0.5239435  ,0.24999449 ,0.408372  ],
                [0.538409   ,0.24874538 ,0.52745754],
                [0.52874815 ,0.2665596  ,0.43685415],
                [0.56777716 ,0.25893795 ,0.67274255],
                [0.5162953  ,0.3253845  ,0.58269596],
                [0.6273562  ,0.29776666 ,0.7362492 ],
                [0.3862428  ,0.3361733  ,0.58113074],
                [0.7264918  ,0.30298874 ,0.50891024],
                [0.2957049  ,0.32291692 ,0.38982567],
                [0.83528256 ,0.29812992 ,0.68334866],
                [0.624676   ,0.48061594 ,0.70820355],
                [0.661161   ,0.4238565  ,0.6368067 ],
                [0.71262705 ,0.5649474  ,0.72714627],
                [0.70808595 ,0.30935663 ,0.5671294 ],
                [0.83530754 ,0.6658356  ,0.7600413 ],
                [0.83928216 ,0.30045372 ,0.6693976 ]
            ]),

            'cat_pose' : np.array([
                [0.42507192 ,0.62434125 ,0.47223485],
                [0.4138795  ,0.6155443  ,0.622737  ],
                [0.4134295  ,0.61663604 ,0.6406976 ],
                [0.4192123  ,0.5856035  ,0.41981333],
                [0.41963053 ,0.58445394 ,0.53299093],
                [0.4896332  ,0.55091226 ,0.78742486],
                [0.4885689  ,0.5558085  ,0.76350474],
                [0.6227099  ,0.5376217  ,0.6418005 ],
                [0.63287747 ,0.5378572  ,0.4794791 ],
                [0.71793544 ,0.5400369  ,0.54760516],
                [0.72797793 ,0.5478353  ,0.43782127],
                [0.5823341  ,0.37258905 ,0.5315256 ],
                [0.581557   ,0.38285792 ,0.5653355 ],
                [0.7262654  ,0.34308073 ,0.6716083 ],
                [0.7344936  ,0.34495473 ,0.7154772 ],
                [0.69802547 ,0.1852346  ,0.4664447 ],
                [0.7066649  ,0.18684557 ,0.5983715 ]
            ]),

            'bridge_pose' : np.array([
                [0.47917593 ,0.2078704  ,0.5528486 ],
                [0.48911938 ,0.19384027 ,0.51077867],
                [0.4950975  ,0.19398823 ,0.5609367 ],
                [0.5236504  ,0.19333301 ,0.59090954],
                [0.5397299  ,0.19526017 ,0.5540197 ],
                [0.5214976  ,0.29290435 ,0.58885694],
                [0.53452504 ,0.274648   ,0.5454867 ],
                [0.5560215  ,0.4339469  ,0.45251495],
                [0.5701454  ,0.43218768 ,0.5345852 ],
                [0.5366786  ,0.53247994 ,0.24764696],
                [0.5474763  ,0.5537294  ,0.10547084],
                [0.33775553 ,0.49930286 ,0.6499475 ],
                [0.35018533 ,0.51240474 ,0.48733962],
                [0.31444657 ,0.70899165 ,0.5221928 ],
                [0.3205527  ,0.714103   ,0.66848195],
                [0.52990484 ,0.67300355 ,0.69654024],
                [0.5451871  ,0.66715956 ,0.71035683]
            ]),

            'standing_forward_bend' : np.array([
                [0.6093226  ,0.36196005 ,0.5605879 ],
                [0.62574095 ,0.3492658  ,0.478875  ],
                [0.6248113  ,0.34992132 ,0.45723727],
                [0.59064835 ,0.30695063 ,0.41697738],
                [0.59232324 ,0.3033098  ,0.47926834],
                [0.5088794  ,0.30035058 ,0.52994156],
                [0.51288307 ,0.30479997 ,0.61167216],
                [0.64659506 ,0.42919403 ,0.49143952],
                [0.63929176 ,0.39708382 ,0.34535342],
                [0.81963205 ,0.44356915 ,0.4945129 ],
                [0.7674484  ,0.43103606 ,0.25968   ],
                [0.2489675  ,0.49035296 ,0.79692656],
                [0.25011486 ,0.48536247 ,0.7108269 ],
                [0.5409963  ,0.4747871  ,0.6389468 ],
                [0.5447976  ,0.4676851  ,0.49088356],
                [0.8210343  ,0.45810038 ,0.48205486],
                [0.78832495 ,0.4566486  ,0.4311303 ]
            ]),

            'puppy_pose' : np.array([
                [0.5417774  ,0.6924896  ,0.45521834],
                [0.53632396 ,0.70731986 ,0.387238  ],
                [0.536082   ,0.7036953  ,0.42571533],
                [0.5058427  ,0.6942115  ,0.5285063 ],
                [0.5110804  ,0.69768655 ,0.5711683 ],
                [0.46058795 ,0.6492716  ,0.57356745],
                [0.48322886 ,0.6455604  ,0.5938966 ],
                [0.5333825  ,0.7300564  ,0.25779885],
                [0.560254   ,0.7509784  ,0.50484717],
                [0.5738956  ,0.8820741  ,0.11343967],
                [0.5915215  ,0.90123004 ,0.41585076],
                [0.32938945 ,0.40247616 ,0.70618856],
                [0.3363493  ,0.40054724 ,0.44321877],
                [0.53873026 ,0.36152443 ,0.6272564 ],
                [0.5570407  ,0.339938   ,0.7965539 ],
                [0.49824548 ,0.1467891  ,0.49824053],
                [0.5201909  ,0.09186977 ,0.74262106]
            ]),

            'plough_pose' : np.array([
                [0.6119883  ,0.52400154 ,0.24878629],
                [0.63230515 ,0.5243803  ,0.36528307],
                [0.6289021  ,0.52776897 ,0.43936396],
                [0.6863636  ,0.5037558  ,0.3260224 ],
                [0.68340653 ,0.5174446  ,0.38250858],
                [0.69013995 ,0.4385169  ,0.6554566 ],
                [0.6846012  ,0.43634996 ,0.70782065],
                [0.70515573 ,0.3285663  ,0.44212025],
                [0.70156395 ,0.34100777 ,0.3943797 ],
                [0.69217193 ,0.2074958  ,0.2595227 ],
                [0.68881035 ,0.17734723 ,0.51246095],
                [0.46391505 ,0.42985767 ,0.6983825 ],
                [0.47538742 ,0.42755935 ,0.66656464],
                [0.5681116  ,0.6035024  ,0.6104876 ],
                [0.5675279  ,0.6030615  ,0.43601766],
                [0.6570858  ,0.77574176 ,0.5565374 ],
                [0.65690166 ,0.7584364  ,0.32584167]
            ])
        }
        print("ExpectedKeypoints object created.")