
# PROJECT TORHANDO - ROBOTIC ARM SEGMENT

Brief Intro: This segment of the project deals with attaching a 2 Degree of Freedom robotic arm to the turtlebot to perform pick and place operation of a table tennis ball (fixed payload).
One DOF would be a turning pair between link 1 and link 2 and the other DOF would be the grasping movement of the gripper.
The entire robotic arm including the gripper will be 3D printed and assembled together.

Base:

To make this arm as a completely independent segment, a balsa wood plate of dimension 13.2x10x3 has been cut such that it can be attached to the upper plate of the turtlebot using removable double tape. 

An area in this plate has been marked such that the base of the manipulator (circular in shape having diameter 7.5 cm) can be stuck using suitable adhesives. Hence when the robotic arm is to be disassembled from the turtlebot, it could be done so without any damage to the arm or turtlebot.



Link 1: 
Link 1 of the robotic arm has a complex geometry and a large thickness which takes a quite a lot of time to 3D print.
The reason behind this complex design is the need to accomodate the base, servo motor, servo extension shaft and the second link.
It would even consist of the text "TORHANDO" for aesthetic purposes, negatively extruded to produce a cut.

Link 2:
Link 2 of the robotic arm is a simple design with hollow space at the center for light weight. The end of this link is made flat to make space to fit the gripper.

The entire geometries of both links together has been assembled in such a way that maximum reach can be attained to pick the payload. This was found by using line diagrams and testing for extension.

## Screenshots

![App Screenshot](https://lh3.googleusercontent.com/74PSOzvtUd_FvZyNNgLPXXEMUWdhdCRV9WVBpJNbJE9BHFooPFBat2xR9TqeaVxBKwaXkbIQUSbVuesCpAlsHYMuRYOFb5Xmz-uj1v8rRTBBqXrzp-8O-WpnrxNPscUV7f_8bnEdDoOwSWD733xxQdYApyBJ85DgTiTmqF7yVYsoJa75MPdPUFEqfBv53bo2XjyGK9G05a6izNLgF6wq_b43MZcNceUpidt3JzOjzpY3VDnI5xP-WwR8zZbfdw2-N_GBFbYNivlPTnII7NqwqGjpsuq8WEPLzkAq05n8zGA9xHTG5KCNBBXQ8i9UVFETJ83WJhGV83LvwPKjk9ymmb5kckiSUhGqNp2iim_gq8QA9GwmKglnvCilXHv5wtCMbvXN9Bn_TseldtVziMYAoMLFz1W26md3it2Wsrvbq2zHkMdQTg7xZ4otabN0DjDl49jP4ymoyIJkVDVAww4qPzla_HBgaADJWwO2VKIMCb8pHoQrr900bTRBNU6zSibhozESqB2tZr8sebiuUFzdptvy1yaZWdum6yZmpqLmjC48hGyY31Xej8WPJN19C6zSNM_AjFGzb8YTt3TlmI-jOKDttqLhU4AGWzXmX4Q2BHPnkB3gLRAPRDGLv8ezS-0jKJWvhsSZYg2dPs6vfkxBFCPUJ0iL_OflLHHSE70XBQ_Z4D1JtjTRB9p_DALh9W7rXjsu3k1RqOyBko0GBOuvuGc=w641-h854-no?authuser=0)


![App Screenshot](https://lh3.googleusercontent.com/7jOB-WDB7RMF_7YO_MvKQqiEbQqY2RhrjDs5SXxaz40YeRy0JVquBJXbkkp9DL8gVvodBWd0FAl83ThR2QyRCRvY21n3J__Qy_zzM6xqVvX2zmB_rhrbWIjlcbxx70cMvguUhJBMENJNsTaP-HqLFt9M2-nDICFcQtu6Y0v50CouHiRtQ-DgmLiVVA5IV2gAB6hsXYF7wcpRCjQlYP_rP3E8nvMFSNL3czDqM-JLnNzx9gBXLjjFk7NznqQyY7eqmbc7KW2tMbuIizUBdpjPySg6LK77MmdiBuu-oyCg6GKakgAh8ba8iMMeJLiJ3hyStML3kZPxdoAecPSkQvfx9hjzTuHmgD00_PRDxhb1O7LlUK-Pveh8hiPQSSIFKkV0MJKV2HOTvXlqJEUcyqAcxgV875Xldc6lyGK8rmhWU80FssKgV18JzTSsYG4eg8tGG1rfBZDXVH6p5x0D2Twt8PvfRdy9Tm0q7yFJ06rgU8ut2zjmWT-Nb4jtf7C3Y9OilceIVGMhxwqN0rUZbA4tzPMsoJE92-NJjdAzfl6stv0_fAqzPEv_SNA6tSWbYlIZhh2CE_bfmfEqX2BGzFaeMpcCdIfHs-zip5dxzE1H6rOr9rdsgKCeaPSxRD19hiE0u0zFZ7jzz2jERvsu1VTY9xJ6qfIHEy1ZWg28I0kkxSKtKXmjxN0ntPNhe_0W6Le6dFPt9b3Tuvs9KPOBBwsvEbE=w1389-h837-no?authuser=0
)

![App Screenshot](https://lh3.googleusercontent.com/pw/AM-JKLV_u5L1P18KYyA1Jy0RXQLmKI7xDeSgXr6CTTB0UQSYdT9-ZeOveZEoG6CTxsxX6UUd6sVJPtkKzATXn4Q4eR_0GtA1xDUmZWDS3olULBoK_-Wp_h88DE6ZpWWRG45xhFL6XCGih8x1LWDRNjjApuDCcwhlt3h4nSN2sHwCGB4rQDmlaMyaAiRwzN-IQMVUtO5-ySdCoqMeWkry7yRx50wwjTCLeKE0vIxaj1aeX8HY5wuBnsgm0hvbHYRC5NybGz5bjdjxvqmR89SI9oajSm5t5rX-jPcy1Y0FD_5LCPHJtAQKToRdgByIHmpdjKgsfVEoIG1CT4ObI3NuwDPtgjxRiaDDi9ycNSE7vbkMmzV6AvG_D4Tp8Fj63LE6mhP2wUStTD3tD8Me3IKm-UuRSREoxBTIJesOgz0q2f4mvXsOHAhWJDMMWAgcs7o78wKnXiC_NbfsP61sfx4AbNklXmfrYGucp11YmnJ1vYorNWpo99fJDZ6LuFWdv96fr2hVjWXg4biCfA5hTidzu21R3PrEgjFuXaH1ZTmcx4hiaoWZZb3c4N07xBJJnbxDRVBQuOhJwOIUqWaIjYT0KkQ6doTRu6EjgRz2Jz9qo8T4ljbQ_pV98OlsJQJ7YDHFOqsY3T_r_Dm474Q564UDJp2O4MevOgP-eL2gh67CZ99GYnYk1F7fGs0iQZvY_4jpWcmhaMgYIs-wTadcnY0nyBsXIPz9oZ33BIy570QTNf-6MNqB_A=w359-h249-no?authuser=0)


