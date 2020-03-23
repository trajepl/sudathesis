import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

plt.style.use('./tickstyle')
with plt.style.context(('./tickstyle')):
    x1 = np.linspace(0, 1, 11)
    y1 = [0.52, 0.55, 0.57, 0.60, 0.62, 0.63, 0.60, 0.59, 0.58, 0.54, 0.53]

    fig, (ax2) = plt.subplots(nrows=1, ncols=1, figsize=(11, 5))

    # ax1.set_xlabel(r'$\alpha$', fontsize=17)
    # ax1.set_ylabel(r'$Spearman\ correlation\  (\rho$)', fontsize=17)
    # ax1.set_ylim(0.4,0.7)
    # ax1.plot(x1, y1, 'ro-')


    # y21 = [0.836, 0.843, 0.860, 0.837, 0.802, 0.778, 0.725, 0.682, 0.677, 0.654, 0.632]
    # y22 = [0.812, 0.834, 0.857, 0.833, 0.794, 0.768, 0.711, 0.675, 0.650, 0.623, 0.593]
    # y23 = [0.645, 0.733, 0.826, 0.814, 0.735, 0.640, 0.602, 0.595, 0.573, 0.541, 0.527]


    # ax2.set_title('Performance with various value of lambda')
    # ax2.set_ylim(0,1)

    data = [
        [
            [(0.8446090567555143, 0.7721976308676449), (0.8354000676855232, 0.7773822311637351), (0.8260821646421022, 0.7794486347887679), (0.8013798154300135, 0.7775922212095021), (0.7844664952487636, 0.7710221297022982), (0.7486369617069051, 0.7590584437123896), (0.7301658357194875, 0.7412459336076321), (0.7194837387629085, 0.7174597242592768), (0.6718593898314942, 0.6879711069632546), (0.638922924215376, 0.6534471975672167), (0.6097697012713792, 0.6148775134942549)], 
            [(0.6351396815432542, 0.5801430579864283), (0.6729721082644712, 0.6058932238414586), (0.7039056807012309, 0.6279040208037736), (0.7072438360001618, 0.6450774822385654), (0.6998998943425139, 0.6565970705246506), (0.6889952536993396, 0.662072812247552), (0.6642929044872508, 0.6616022950820342), (0.6536108075306719, 0.6557270143687974), (0.6404807300215437, 0.6453051247404292), (0.6226772350939122, 0.6313491349592588), (0.6097697012713792, 0.6148775134942549)]
        ], 
        [
            [(0.8163824154632461, 0.7630780484678373), (0.8193937557222672, 0.770512584088817), (0.8257534384074399, 0.7758811373635449), (0.8262342391602708, 0.7785504709267465), (0.8144109115565649, 0.7778366246015832), (0.7984133592350995, 0.7730538164823639), (0.7750071044041031, 0.763585064478796), (0.7455252764236978, 0.7489680688610421), (0.7256157543405627, 0.7289813897731288), (0.6925279207139253, 0.7037095194696471), (0.6762462588566963, 0.6735657810729306)], 
            [(0.652202420301881, 0.5986693030248839), (0.6839390709019911, 0.6267846772683694), (0.7015538621193423, 0.6513429728618513), (0.7114976958710728, 0.6714308490364368), (0.7257031726592592, 0.6863848686682653), (0.721878621216286, 0.6958861372364222), (0.7095089291207267, 0.699993166418204), (0.7083506363979976, 0.699105425792499), (0.6941014504504629, 0.6938736030601825), (0.68573114643527, 0.6850867070514065), (0.6762462588566963, 0.6735657810729306)]
        ], 
        [
            [(0.3972417416425566, 0.3665923280432426), (0.43136137971878225, 0.4010295204992122), (0.4618372568519238, 0.4368321215764763), (0.4873253959900367, 0.4725481891804073), (0.5109896312656711, 0.5060543733193701), (0.5282455814799502, 0.5347258986537865), (0.542680489455061, 0.5559335591756328), (0.5495371457673299, 0.5677729322443725), (0.5461460568419527, 0.5696799481993391), (0.5405388926679162, 0.5625571600689917), (0.5327354323238274, 0.5483502272978049)], 
            [(0.5151777488552066, 0.4733642191146443), (0.562461886988907, 0.5173811016868657), (0.590446282254711, 0.5542905303537781), (0.6019963093093552, 0.5814886577853106), (0.600541114753606, 0.5978286755229981), (0.5957204758709501, 0.6038359835464471), (0.5870565574037205, 0.6012823100127263), (0.5750101436797503, 0.5924638601283412), (0.5625577814182932, 0.5795886877000983), (0.547894527390846, 0.5644504542720048), (0.5327354323238274, 0.5483502272978049)]
        ]
    ]

    rls = [[], [], []]
    for idx, item in enumerate(data):
        for tup in item[1]:
            rls[idx].append(tup[0])

    ax2.set_xlabel(r'$\lambda$', fontsize=18)
    ax2.set_ylabel(r'$Spearman\ correlation\  (\rho$)', fontsize=18)
    ax2.plot(x1, rls[0], 'b*-', label='MC',)
    ax2.plot(x1, rls[1], 'ro-', label='RG')
    ax2.plot(x1, rls[2], 'g.-', label='WS353')
    ax2.legend()

plt.grid(axis='y')
# plt.show()
plt.savefig('./test.pdf', format='pdf')