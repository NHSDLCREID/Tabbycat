# Generated by Django 4.1.7 on 2024-03-26 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participants', '0021_team_seed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='code_name',
            field=models.CharField(blank=True, help_text='Name used to obscure real name on public-facing pages', max_length=25, verbose_name='code name'),
        ),
        migrations.AlterField(
            model_name='team',
            name='emoji',
            field=models.CharField(blank=True, choices=[('☺️', '☺️ White Smiling'), ('☹', '☹ White Frowning'), ('☝️', '☝️ White Up Pointing Index'), ('✌️', '✌️ Victory Hand'), ('✍', '✍ Writing Hand'), ('❤️', '❤️ Heavy Black Heart'), ('❣', '❣ Heart Exclamation Mark'), ('☠', '☠ Skull and Crossbones'), ('♨️', '♨️ Hot Springs'), ('✈️', '✈️ Airplane'), ('⌛', '⌛ Hourglass'), ('⌚', '⌚ Watch'), ('♈', '♈ Aries'), ('♉', '♉ Taurus'), ('♊', '♊ Gemini'), ('♋', '♋ Cancer'), ('♌', '♌ Leo'), ('♍', '♍ Virgo'), ('♎', '♎ Libra'), ('♏', '♏ Scorpius'), ('♐', '♐ Sagittarius'), ('♑', '♑ Capricorn'), ('♒', '♒ Aquarius'), ('♓', '♓ Pisces'), ('☀️', '☀️ Black Sun With Rays'), ('☁️', '☁️ Cloud'), ('☂', '☂ Umbrella'), ('❄️', '❄️ Snowflake'), ('☃', '☃ Snowman'), ('☄️', '☄️ Comet'), ('♠️', '♠️ Spade Suit'), ('♥️', '♥️ Heart Suit'), ('♦️', '♦️ Diamond Suit'), ('♣️', '♣️ Club Suit'), ('▶️', '▶️ Black Right-Pointing Triangle'), ('◀️', '◀️ Black Left-Pointing Triangle'), ('☎️', '☎️ Black Telephone'), ('⌨', '⌨ Keyboard'), ('✉️', '✉️ Envelope'), ('✏️', '✏️ Pencil'), ('✒️', '✒️ Black Nib'), ('✂️', '✂️ Scissors'), ('↗️', '↗️ North East Arrow'), ('➡️', '➡️ Black Rightwards Arrow'), ('↘️', '↘️ South East Arrow'), ('↙️', '↙️ South West Arrow'), ('↖️', '↖️ North West Arrow'), ('↕️', '↕️ Up Down Arrow'), ('↔️', '↔️ Left Right Arrow'), ('↩️', '↩️ Leftwards Arrow With Hook'), ('↪️', '↪️ Rightwards Arrow With Hook'), ('✡', '✡ Star of David'), ('☸', '☸ Wheel of Dharma'), ('☯', '☯ Yin Yang'), ('✝', '✝ Latin Cross'), ('☦', '☦ Orthodox Cross'), ('☪', '☪ Star and Crescent'), ('☮', '☮ Peace Symbol'), ('☢', '☢ Radioactive Sign'), ('☣', '☣ Biohazard Sign'), ('☑️', '☑️ Ballot Box With Check'), ('✔️', '✔️ Heavy Check Mark'), ('✖️', '✖️ Heavy Multiplication X'), ('✳️', '✳️ Eight Spoked Asterisk'), ('✴️', '✴️ Eight Pointed Black Star'), ('❇️', '❇️ Sparkle'), ('‼️', '‼️ Double Exclamation Mark'), ('〰️', '〰️ Wavy Dash'), ('©️', '©️ Copyright Sign'), ('®️', '®️ Registered Sign'), ('™️', '™️ Trade Mark Sign'), ('Ⓜ️', 'Ⓜ️ Capital M'), ('㊗️', '㊗️ Congratulations'), ('㊙️', '㊙️ Secret'), ('▪️', '▪️ Black Square'), ('▫️', '▫️ White Square'), ('#⃣️', '#⃣️ Keycap Number Sign'), ('*⃣', '*⃣ Keycap Asterisk'), ('0⃣️', '0⃣️ Keycap Digit Zero'), ('1⃣️', '1⃣️ Keycap Digit One'), ('2⃣️', '2⃣️ Keycap Digit Two'), ('3⃣️', '3⃣️ Keycap Digit Three'), ('4⃣️', '4⃣️ Keycap Digit Four'), ('5⃣️', '5⃣️ Keycap Digit Five'), ('6⃣️', '6⃣️ Keycap Digit Six'), ('7⃣️', '7⃣️ Keycap Digit Seven'), ('8⃣️', '8⃣️ Keycap Digit Eight'), ('9⃣️', '9⃣️ Keycap Digit Nine'), ('⁉️', '⁉️ Exclamation Question Mark'), ('ℹ️', 'ℹ️ Information Source'), ('⤴️', '⤴️ Right-Curve-Up'), ('⤵️', '⤵️ Right-Curve-Down'), ('♻️', '♻️ Recycling'), ('〽️', '〽️ Part Alternation Mark'), ('◻️', '◻️ White Medium Square'), ('◼️', '◼️ Black Medium Square'), ('◽', '◽ White Medium Small Square'), ('◾', '◾ Black Medium Small Square'), ('☕', '☕ Hot Beverage'), ('⚠️', '⚠️ Warning Sign'), ('☔', '☔ Umbrella With Rain Drops'), ('⏏', '⏏ Eject Symbol'), ('⬆️', '⬆️ Upwards Black Arrow'), ('⬇️', '⬇️ Downwards Black Arrow'), ('⬅️', '⬅️ Leftwards Black Arrow'), ('⚡', '⚡ High Voltage'), ('☘', '☘ Shamrock'), ('⚓', '⚓ Anchor'), ('♿', '♿ Wheelchair Symbol'), ('⚒', '⚒ Hammer and Pick'), ('⚙', '⚙ Gear'), ('⚗', '⚗ Alembic'), ('⚖', '⚖ Scales'), ('⚔', '⚔ Crossed Swords'), ('⚰', '⚰ Coffin'), ('⚱', '⚱ Funeral Urn'), ('⚜', '⚜ Fleur-De-Lis'), ('⚛', '⚛ Atom Symbol'), ('⚪', '⚪ Medium White Circle'), ('⚫', '⚫ Medium Black Circle'), ('🀄', '🀄 Mahjong Tile Red Dragon'), ('⭐', '⭐ White Medium Star'), ('⬛', '⬛ Black Square'), ('⬜', '⬜ White Square'), ('⛑', '⛑ Rescue Hat'), ('⛰', '⛰ Mountain'), ('⛪', '⛪ Church'), ('⛲', '⛲ Fountain'), ('⛺', '⛺ Tent'), ('⛽', '⛽ Fuel Pump'), ('⛵', '⛵ Sailboat'), ('⛴', '⛴ Ferry'), ('⛔', '⛔ No Entry'), ('⛅', '⛅ Overcast'), ('⛈', '⛈ Storm'), ('⛱', '⛱ Umbrella'), ('⛄', '⛄ Snowman'), ('⚽', '⚽ Soccer'), ('⚾', '⚾ Baseball'), ('⛳', '⛳ Hole in One'), ('⛸', '⛸ Ice Skate'), ('⛷', '⛷ Skier'), ('⛹', '⛹ Person With Ball'), ('⛏', '⛏ Pick'), ('⛓', '⛓ Chains'), ('⛩', '⛩ Shinto Shrine'), ('⭕', '⭕ Heavy Large Circle'), ('❗', '❗ Heavy Exclamation Mark'), ('🅿️', '🅿️ Squared P'), ('🈯', '🈯 Squared 指 (Finger)'), ('🈚', '🈚 Squared CJK Unified Ideograph-7121'), ('😁', '😁 Smiling Eyes'), ('😂', '😂 Joy Tears'), ('😃', '😃 Smiling Face With Open Mouth'), ('😄', '😄 Smiling Face With Open Mouth and Smiling Eyes'), ('😅', '😅 Cold Sweat'), ('😆', '😆 Closed Eyes'), ('😉', '😉 Winky'), ('😊', '😊 Smiling Eyes'), ('😋', '😋 Face Savouring Delicious Food'), ('😎', '😎 Shaded Eyes'), ('😍', '😍 Heart Eyes'), ('😘', '😘 Kissy'), ('😚', '😚 Kissing Face With Closed Eyes'), ('😇', '😇 Halo'), ('😐', '😐 Neutral'), ('😶', '😶 No Mouth'), ('😏', '😏 Smirking'), ('😣', '😣 Persevering'), ('😥', '😥 Disappointed'), ('😪', '😪 Sleepy'), ('😫', '😫 Tired'), ('😌', '😌 Relieved'), ('😜', '😜 Tongue Out'), ('😝', '😝 Tongue Out Closed Eyes'), ('😒', '😒 Unamused'), ('😓', '😓 Cold Sweat'), ('😔', '😔 Pensive'), ('😖', '😖 Confounded'), ('😷', '😷 Medical Mask'), ('😲', '😲 Astonished'), ('😞', '😞 Disappointed'), ('😤', '😤 Face With Look of Triumph'), ('😢', '😢 Crying'), ('😭', '😭 Sobbing'), ('😨', '😨 Fearful'), ('😩', '😩 Weary'), ('😰', '😰 Open Mouth Cold Sweat'), ('😱', '😱 Screaming'), ('😳', '😳 Flushed'), ('😵', '😵 Dizzy'), ('😡', '😡 Pouting'), ('😠', '😠 Angry'), ('👿', '👿 Imp'), ('😈', '😈 Smiling Face With Horns'), ('👦', '👦 Boy'), ('👧', '👧 Girl'), ('👨', '👨 Generic Man'), ('👩', '👩 Generic Woman'), ('👴', '👴 Older Man'), ('👵', '👵 Older Woman'), ('👶', '👶 Baby'), ('👱', '👱 Person With Blond Hair'), ('👮', '👮 Police Officer'), ('👲', '👲 Man With Gua Pi Mao'), ('👳', '👳 Man With Turban'), ('👷', '👷 Trade Worker'), ('👸', '👸 Princess'), ('💂', '💂 Guardsman'), ('🎅', '🎅 Santa Claus'), ('👼', '👼 Baby Angel'), ('👯', '👯 Bunny Women'), ('💆', '💆 Face Massage'), ('💇', '💇 Haircut'), ('👰', '👰 Bride'), ('🙍', '🙍 Person Frowning'), ('🙎', '🙎 Person With Pouting'), ('🙅', '🙅 Block Gesture'), ('🙆', '🙆 OK Gesture'), ('💁', '💁 Sass Gesture'), ('🙋', '🙋 Raised Hand'), ('🙇', '🙇 Deep Bow'), ('🙌', '🙌 Praise Hands'), ('🙏', '🙏 Prayer Hands'), ('👤', '👤 Bust in Silhouette'), ('👥', '👥 Busts in Silhouette'), ('🚶', '🚶 Pedestrian'), ('🏃', '🏃 Runner'), ('💃', '💃 Dancer'), ('💏', '💏 Kiss'), ('💑', '💑 Heteronormative Couple'), ('👪', '👪 Hetero Family'), ('👫', '👫 Man & Woman'), ('👬', '👬 Two Men'), ('👭', '👭 Two Women'), ('💪', '💪 Biceps'), ('👈', '👈 Left Pointing Backhand'), ('👉', '👉 Right Pointing Backhand'), ('👆', '👆 Pointing Hand'), ('👇', '👇 Down Pointing Backhand'), ('✊', '✊ Power Hand'), ('✋', '✋ Palm Hand'), ('👊', '👊 Fist Hand'), ('👌', '👌 OK Hand'), ('👍', '👍 Thumbs Up'), ('👎', '👎 Thumbs Down'), ('👋', '👋 Waving Hand Sign'), ('👏', '👏 Clappy Hands'), ('👐', '👐 Open Hands Sign'), ('💅', '💅 Nail Polish'), ('👣', '👣 Footprints'), ('👀', '👀 Eyes'), ('👂', '👂 Ear'), ('👃', '👃 Nose'), ('👅', '👅 Lick'), ('👄', '👄 Mouth'), ('💋', '💋 Kiss Mark'), ('💘', '💘 Cupid Arrow'), ('💓', '💓 Beating Heart'), ('💔', '💔 Broken Heart'), ('💕', '💕 Two Hearts'), ('💖', '💖 Sparkly Heart'), ('💗', '💗 Growing Heart'), ('💙', '💙 Blue Heart'), ('💚', '💚 Green Heart'), ('💛', '💛 Yellow Heart'), ('💜', '💜 Purple Heart'), ('💝', '💝 Heart With Ribbon'), ('💞', '💞 Revolving Hearts'), ('💟', '💟 Heart Decoration'), ('💌', '💌 Love Letter'), ('💧', '💧 Droplet'), ('💤', '💤 ZZZ'), ('💢', '💢 Anger'), ('💣', '💣 Bomb'), ('💥', '💥 Sparks'), ('💦', '💦 Splashing'), ('💨', '💨 Dash'), ('💫', '💫 Shooting Star'), ('💬', '💬 Speech Bubble'), ('💭', '💭 Thinky Cloud'), ('👓', '👓 Eyeglasses'), ('👔', '👔 Business Casual'), ('👕', '👕 T-Shirt'), ('👖', '👖 Jeans'), ('👗', '👗 Dress'), ('👘', '👘 Kimono'), ('👙', '👙 Bikini'), ('👚', '👚 Womans Clothes'), ('👛', '👛 Purse'), ('👜', '👜 Handbag'), ('👝', '👝 Pouch'), ('🎒', '🎒 Backpack'), ('👞', '👞 Mans Shoe'), ('👟', '👟 Running Shoe'), ('👠', '👠 Heels'), ('👡', '👡 Womans Sandal'), ('👢', '👢 Womans Boots'), ('👑', '👑 Crown'), ('👒', "👒 Lady's Hat"), ('🎩', '🎩 Top Hat'), ('💄', '💄 Lipstick'), ('💍', '💍 Proposal'), ('💎', '💎 Gem'), ('👹', '👹 Japanese Ogre'), ('👺', '👺 Japanese Goblin'), ('👻', '👻 Ghost'), ('💀', '💀 Skull'), ('👽', '👽 Alien'), ('👾', '👾 Space Invader'), ('💩', '💩 Pile of Poo'), ('🐵', '🐵 Monkey'), ('🙈', '🙈 See No Evil'), ('🙉', '🙉 Hear No Evil'), ('🙊', '🙊 Speak No Evil'), ('🐒', '🐒 Monkey'), ('🐶', '🐶 Dog'), ('🐕', '🐕 Dog'), ('🐩', '🐩 Poodle'), ('🐺', '🐺 Wolf'), ('🐱', '🐱 Cat'), ('😸', '😸 Grinning Cat with Smiling Eyes'), ('😹', '😹 Cat with Tears of Joy'), ('😺', '😺 Smiling Cat with Open Mouth'), ('😻', '😻 Smiling Cat with Heart Eyes'), ('😼', '😼 Cat with Wry Smile'), ('😽', '😽 Kissing Cat with Closed Eyes'), ('😾', '😾 Pouting Cat Face'), ('😿', '😿 Crying Cat Face'), ('🙀', '🙀 Weary Cat Face'), ('🐈', '🐈 Cat'), ('🐯', '🐯 Tiger'), ('🐅', '🐅 Tiger'), ('🐆', '🐆 Leopard'), ('🐴', '🐴 Horse'), ('🐎', '🐎 Horse'), ('🐮', '🐮 Cow'), ('🐂', '🐂 Ox'), ('🐃', '🐃 Water Buffalo'), ('🐄', '🐄 Cow'), ('🐷', '🐷 Pig'), ('🐖', '🐖 Pig'), ('🐗', '🐗 Boar'), ('🐽', '🐽 Pig Nose'), ('🐏', '🐏 Ram'), ('🐑', '🐑 Sheep'), ('🐐', '🐐 Goat'), ('🐪', '🐪 Dromedary Camel'), ('🐫', '🐫 Bactrian Camel'), ('🐘', '🐘 Elephant'), ('🐭', '🐭 Mouse'), ('🐁', '🐁 Mouse'), ('🐀', '🐀 Rat'), ('🐹', '🐹 Hamster'), ('🐰', '🐰 Rabbit'), ('🐇', '🐇 Rabbit'), ('🐻', '🐻 Bear'), ('🐨', '🐨 Koala'), ('🐼', '🐼 Panda'), ('🐾', '🐾 Paw Prints'), ('🐔', '🐔 Chicken'), ('🐓', '🐓 Rooster'), ('🐣', '🐣 Hatching'), ('🐤', '🐤 Chick'), ('🐥', '🐥 Front-Facing Baby Chick'), ('🐦', '🐦 Bird'), ('🐧', '🐧 Penguin'), ('🐸', '🐸 Frog'), ('🐊', '🐊 Croc'), ('🐢', '🐢 Turtle'), ('🐍', '🐍 Slithering'), ('🐲', '🐲 Dragon'), ('🐉', '🐉 Dragon'), ('🐳', '🐳 Whale'), ('🐋', '🐋 Whale'), ('🐬', '🐬 Dolphin'), ('🐟', '🐟 Fish'), ('🐠', '🐠 Fish'), ('🐡', '🐡 Blowfish'), ('🐙', '🐙 Octopus'), ('🐚', '🐚 Shell'), ('🐌', '🐌 Snail'), ('🐛', '🐛 Bug'), ('🐜', '🐜 Ant'), ('🐝', '🐝 Honeybee'), ('🐞', '🐞 Lady Beetle'), ('💐', '💐 Bouquet'), ('🌸', '🌸 Sakura'), ('💮', '💮 White Flower'), ('🌹', '🌹 Rose'), ('🌺', '🌺 Hibiscus'), ('🌻', '🌻 Sunflower'), ('🌼', '🌼 Blossom'), ('🌷', '🌷 Tulip'), ('🌱', '🌱 Seedling'), ('🌲', '🌲 Evergreen Tree'), ('🌳', '🌳 Deciduous Tree'), ('🌴', '🌴 Palm Tree'), ('🌵', '🌵 Cactus'), ('🌾', '🌾 Ear of Rice'), ('🌿', '🌿 Herb'), ('🍀', '🍀 Clover'), ('🍁', '🍁 Maple Leaf'), ('🍂', '🍂 Fallen Leaf'), ('🍃', '🍃 Blown Leaves'), ('🍇', '🍇 Grapes'), ('🍈', '🍈 Melon'), ('🍉', '🍉 Watermelon'), ('🍊', '🍊 Tangerine'), ('🍋', '🍋 Lemon'), ('🍌', '🍌 Banana'), ('🍍', '🍍 Pineapple'), ('🍎', '🍎 Red Apple'), ('🍏', '🍏 Green Apple'), ('🍐', '🍐 Pear'), ('🍑', '🍑 Peach'), ('🍒', '🍒 Cherries'), ('🍓', '🍓 Strawberry'), ('🍅', '🍅 Tomato'), ('🍆', '🍆 Eggplant'), ('🌽', '🌽 Corn'), ('🍄', '🍄 Mushroom'), ('🌰', '🌰 Chestnut'), ('🍞', '🍞 Bread'), ('🍖', '🍖 Meat on Bone'), ('🍗', '🍗 Poultry Leg'), ('🍔', '🍔 Hamburger'), ('🍟', '🍟 Fries'), ('🍕', '🍕 Pizza'), ('🍲', '🍲 Pot of Food'), ('🍱', '🍱 Bento Box'), ('🍘', '🍘 Rice Cracker'), ('🍙', '🍙 Rice Ball'), ('🍚', '🍚 Cooked Rice'), ('🍛', '🍛 Curry and Rice'), ('🍜', '🍜 Steaming Bowl'), ('🍝', '🍝 Spaghetti'), ('🍠', '🍠 Sweet Potato'), ('🍢', '🍢 Oden'), ('🍣', '🍣 Sushi'), ('🍤', '🍤 Fried Shrimp'), ('🍥', '🍥 Fish Cake With Swirl Design'), ('🍡', '🍡 Dango'), ('🍦', '🍦 Ice Cream'), ('🍧', '🍧 Shaved Ice'), ('🍨', '🍨 Ice Cream'), ('🍩', '🍩 Doughnut'), ('🍪', '🍪 Cookie'), ('🎂', '🎂 Birthday Cake'), ('🍰', '🍰 Shortcake'), ('🍫', '🍫 Chocolate Bar'), ('🍬', '🍬 Candy'), ('🍭', '🍭 Lollipop'), ('🍮', '🍮 Custard'), ('🍯', '🍯 Honey Pot'), ('🍼', '🍼 Baby Bottle'), ('🍵', '🍵 Teacup Without Handle'), ('🍶', '🍶 Sake Bottle and Cup'), ('🍷', '🍷 Wine Glass'), ('🍸', '🍸 Cocktail Glass'), ('🍹', '🍹 Tropical Drink'), ('🍺', '🍺 Beer'), ('🍻', '🍻 Clinking Beer Mugs'), ('🍴', '🍴 Fork & Knife'), ('🍳', '🍳 Cooking'), ('🌍', '🌍 Earth Globe Europe-Africa'), ('🌎', '🌎 Earth Globe Americas'), ('🌏', '🌏 Earth Globe Asia-Australia'), ('🌐', '🌐 Globe With Meridians'), ('🌋', '🌋 Volcano'), ('🗻', '🗻 Mount Fuji'), ('🏠', '🏠 House'), ('🏡', '🏡 House With Garden'), ('🏢', '🏢 Office'), ('🏣', '🏣 Japanese Post Office'), ('🏤', '🏤 European Post Office'), ('🏥', '🏥 Hospital'), ('🏦', '🏦 Bank'), ('🏨', '🏨 Hotel'), ('🏩', '🏩 Love Hotel'), ('🏪', '🏪 Convenience Store'), ('🏫', '🏫 School'), ('🏬', '🏬 Department Store'), ('🏭', '🏭 Factory'), ('🏯', '🏯 Japanese Castle'), ('🏰', '🏰 Castle'), ('💒', '💒 Wedding'), ('🗼', '🗼 Tokyo Tower'), ('🗽', '🗽 Liberty'), ('🗾', '🗾 Silhouette of Japan'), ('🌁', '🌁 Foggy'), ('🌃', '🌃 Night With Stars'), ('🌄', '🌄 Sunrise Over Mountains'), ('🌅', '🌅 Sunrise'), ('🌆', '🌆 Cityscape at Dusk'), ('🌇', '🌇 Sunset Over Buildings'), ('🌉', '🌉 Bridge at Night'), ('🌊', '🌊 Big Wave'), ('🗿', '🗿 Moyai'), ('🌌', '🌌 Milky Way'), ('🎠', '🎠 Carousel Horse'), ('🎡', '🎡 Ferris Wheel'), ('🎢', '🎢 Roller Coaster'), ('💈', '💈 Barber Pole'), ('🎪', '🎪 Circus Tent'), ('🎭', '🎭 Performing Arts'), ('🎨', '🎨 Palette'), ('🎰', '🎰 Slot Machine'), ('🚂', '🚂 Steam Locomotive'), ('🚃', '🚃 Railcar'), ('🚄', '🚄 Fast Train'), ('🚅', '🚅 Fast Train with Bullet Nose'), ('🚆', '🚆 Train'), ('🚇', '🚇 Metro'), ('🚈', '🚈 Light Rail'), ('🚉', '🚉 Station'), ('🚊', '🚊 Tram'), ('🚝', '🚝 Monorail'), ('🚞', '🚞 Mountain Railway'), ('🚋', '🚋 Tram Car'), ('🚌', '🚌 Bus'), ('🚍', '🚍 Bus'), ('🚎', '🚎 Trolleybus'), ('🚏', '🚏 Bus Stop'), ('🚐', '🚐 Minibus'), ('🚑', '🚑 Ambulance'), ('🚒', '🚒 Fire Engine'), ('🚓', '🚓 Police Car'), ('🚔', '🚔 Police Car'), ('🚕', '🚕 Taxi'), ('🚖', '🚖 Oncoming Taxi'), ('🚗', '🚗 Automobile'), ('🚘', '🚘 Automobile'), ('🚙', '🚙 Recreational Vehicle'), ('🚚', '🚚 Truck'), ('🚛', '🚛 Articulated Lorry'), ('🚜', '🚜 Tractor'), ('🚲', '🚲 Bicycle'), ('🚳', '🚳 No Bicycles'), ('🚨', '🚨 Alert Light'), ('🔱', '🔱 Trident'), ('🚣', '🚣 Rowboat'), ('🚤', '🚤 Speedboat'), ('🚢', '🚢 Ship'), ('💺', '💺 Seat'), ('🚁', '🚁 Helicopter'), ('🚟', '🚟 Suspension Railway'), ('🚠', '🚠 Sky Tram'), ('🚡', '🚡 Aerial Tramway'), ('🚀', '🚀 Rocket'), ('🏧', '🏧 ATM'), ('🚮', '🚮 Put Litter in Its Place'), ('🚥', '🚥 Horizontal Traffic Light'), ('🚦', '🚦 Traffic Light'), ('🚧', '🚧 Hazard Sign'), ('🚫', '🚫 Prohibited'), ('🚭', '🚭 No Smoking'), ('🚯', '🚯 Do Not Litter'), ('🚰', '🚰 Tap Water'), ('🚱', '🚱 Non-Potable Water'), ('🚷', '🚷 No Pedestrians'), ('🚸', '🚸 Children Crossing'), ('🚹', '🚹 Mens Symbol'), ('🚺', '🚺 Womens Symbol'), ('🚻', '🚻 Restroom'), ('🚼', '🚼 Baby Symbol'), ('🚾', '🚾 Water Closet'), ('🛂', '🛂 Passport Control'), ('🛃', '🛃 Customs'), ('🛄', '🛄 Baggage Claim'), ('🛅', '🛅 Left Luggage'), ('🚪', '🚪 Door'), ('🚽', '🚽 Toilet'), ('🚿', '🚿 Shower'), ('🛀', '🛀 Bath'), ('🛁', '🛁 Bathtub'), ('⏳', '⏳ Hourglass'), ('⏰', '⏰ Alarm Clock'), ('⏱', '⏱ Stopwatch'), ('⏲', '⏲ Timer Clock'), ('🕛', "🕛 Twelve O'Clock"), ('🕧', '🕧 Half Past Twelve'), ('🕐', "🕐 One O'Clock"), ('🕜', '🕜 Half Past One'), ('🕑', "🕑 Two O'Clock"), ('🕝', '🕝 Half Past Two'), ('🕒', "🕒 Three O'Clock"), ('🕞', '🕞 Half Past Three'), ('🕓', "🕓 Four O'Clock"), ('🕟', '🕟 Half Past Four'), ('🕔', "🕔 Five O'Clock"), ('🕠', '🕠 Half Past Five'), ('🕕', "🕕 Six O'Clock"), ('🕡', '🕡 Half Past Six'), ('🕖', "🕖 Seven O'Clock"), ('🕢', '🕢 Half Past Seven'), ('🕗', "🕗 Eight O'Clock"), ('🕣', '🕣 Half Past Eight'), ('🕘', "🕘 Nine O'Clock"), ('🕤', '🕤 Half Past Nine'), ('🕙', "🕙 Ten O'Clock"), ('🕥', '🕥 Half Past Ten'), ('🕚', "🕚 Eleven O'Clock"), ('🕦', '🕦 Half Past Eleven'), ('⛎', '⛎ Ophiuchus'), ('🌑', '🌑 New Moon'), ('🌒', '🌒 Waxing Crescent'), ('🌓', '🌓 First Quarter Moon Symbol'), ('🌔', '🌔 Waxing Gibbous'), ('🌕', '🌕 Full Moon'), ('🌖', '🌖 Waning Gibbous'), ('🌗', '🌗 Half Moon'), ('🌘', '🌘 Waning Crescent'), ('🌙', '🌙 Crescent Moon'), ('🌚', '🌚 New Moon With Face'), ('🌛', '🌛 First Quarter Moon With Face'), ('🌜', '🌜 Last Quarter Moon With Face'), ('🌝', '🌝 Full Moon With Face'), ('🌞', '🌞 Sun'), ('🌀', '🌀 Cyclone'), ('🌈', '🌈 Rainbow'), ('🌂', '🌂 Umbrella'), ('🌟', '🌟 Glowing Star'), ('🌠', '🌠 Shooting Star'), ('🔥', '🔥 Fire'), ('🎃', '🎃 Jack-O-Lantern'), ('🎄', '🎄 Presents Tree'), ('🎆', '🎆 Fireworks'), ('🎇', '🎇 Firework Sparkler'), ('✨', '✨ Sparkles'), ('🎈', '🎈 Balloon'), ('🎉', '🎉 Party Pop'), ('🎊', '🎊 Confetti Ball'), ('🎋', '🎋 Tanabata Tree'), ('🎌', '🎌 Crossed Flags'), ('🎍', '🎍 Pine Decoration'), ('🎎', '🎎 Japanese Dolls'), ('🎏', '🎏 Carp Streamer'), ('🎐', '🎐 Wind Chime'), ('🎑', '🎑 Moon Viewing Ceremony'), ('🎓', '🎓 Grad Cap'), ('🎯', '🎯 Bullseye'), ('🎴', '🎴 Flower Playing Cards'), ('🎀', '🎀 Ribbon'), ('🎁', '🎁 Wrapped Present'), ('🎫', '🎫 Ticket'), ('🏀', '🏀 Basketball'), ('🏈', '🏈 America Ball'), ('🏉', '🏉 Rugby Ball'), ('🎾', '🎾 Tennis'), ('🎱', '🎱 Billiards'), ('🎳', '🎳 Bowling'), ('🎣', '🎣 Fishing Pole and Fish'), ('🎽', '🎽 Running Shirt With Sash'), ('🎿', '🎿 Ski and Ski Boot'), ('🏂', '🏂 Snowboarder'), ('🏄', '🏄 Surfer'), ('🏇', '🏇 Horse Racing'), ('🏊', '🏊 Swimmer'), ('🚴', '🚴 Bicyclist'), ('🚵', '🚵 Mountain Bicyclist'), ('🏆', '🏆 Trophy'), ('🎮', '🎮 Video Game'), ('🎲', '🎲 Random Cube'), ('🃏', '🃏 Playing Card Black Joker'), ('🔇', '🔇 Speaker With Cancellation Stroke'), ('🔈', '🔈 Speaker'), ('🔉', '🔉 Speaker With One Sound Wave'), ('🔊', '🔊 Speaker With Three Sound Waves'), ('📢', '📢 Public Address Loudspeaker'), ('📣', '📣 Loud Phone'), ('📯', '📯 Horn'), ('🔔', '🔔 Bell'), ('🔕', '🔕 No Bells'), ('🔀', '🔀 Shuffle'), ('🔁', '🔁 Repeat'), ('🔂', '🔂 Repeat Once'), ('⏩', '⏩ Fast Forward'), ('⏭', '⏭ Next Track'), ('⏯', '⏯ Play/Pause'), ('⏪', '⏪ Rewind'), ('⏮', '⏮ Previous Track'), ('🔼', '🔼 Up-Pointing Small Red Triangle'), ('⏫', '⏫ Up to Top'), ('🔽', '🔽 Down-Pointing Small Red Triangle'), ('⏬', '⏬ Down to Bottom'), ('🎼', '🎼 Musical Score'), ('🎵', '🎵 Musical Note'), ('🎶', '🎶 Music Notes'), ('🎤', '🎤 Microphone'), ('🎧', '🎧 Headphone'), ('🎷', '🎷 Saxophone'), ('🎸', '🎸 Guitar'), ('🎹', '🎹 Keyboard'), ('🎺', '🎺 Trumpet'), ('🎻', '🎻 Violin'), ('📻', '📻 Boom Box'), ('📱', '📱 Internet Phone'), ('📳', '📳 Vibration Mode'), ('📴', '📴 Mobile Phone Off'), ('📲', '📲 Download to Phone'), ('📵', '📵 No Mobile Phones'), ('📞', '📞 Old Phone'), ('🔟', '🔟 Keycap Ten'), ('📶', '📶 Antenna With Bars'), ('📟', '📟 Pager'), ('📠', '📠 Fax Machine'), ('🔋', '🔋 Battery'), ('🔌', '🔌 Plug'), ('💻', '💻 Personal Computer'), ('💽', '💽 Minidisc'), ('💾', '💾 Floppy'), ('💿', '💿 Compact Disc'), ('📀', '📀 DVD'), ('🎥', '🎥 Movie Camera'), ('🎦', '🎦 Cinema'), ('🎬', '🎬 Clapper'), ('📺', '📺 Television'), ('📷', '📷 Camera'), ('📹', '📹 Video Camera'), ('📼', '📼 Videocassette'), ('🔅', '🔅 Low Brightness Symbol'), ('🔆', '🔆 High Brightness Symbol'), ('🔍', '🔍 Bigger Glass'), ('🔎', '🔎 Right-Pointing Magnifying Glass'), ('🔬', '🔬 Microscope'), ('🔭', '🔭 Telescope'), ('📡', '📡 Satellite Dish'), ('💡', '💡 Light Bulb'), ('🔦', '🔦 Electric Torch'), ('🏮', '🏮 Izakaya Lantern'), ('📔', '📔 Notebook With Decorative Cover'), ('📕', '📕 Closed Book'), ('📖', '📖 Open Book'), ('📗', '📗 Green Book'), ('📘', '📘 Blue Book'), ('📙', '📙 Orange Book'), ('📚', '📚 Books'), ('📓', '📓 Notebook'), ('📒', '📒 Ledger'), ('📃', '📃 Page With Curl'), ('📜', '📜 Scroll'), ('📄', '📄 Page Facing Up'), ('📰', '📰 Newspaper'), ('📑', '📑 Bookmark Tabs'), ('🔖', '🔖 Bookmark'), ('💰', '💰 Money Bag'), ('💴', '💴 Banknote With Yen Sign'), ('💵', '💵 Banknote With Dollar Sign'), ('💶', '💶 Banknote With Euro Sign'), ('💷', '💷 Banknote With Pound Sign'), ('💸', '💸 Flying Money'), ('💱', '💱 Currency Exchange'), ('💲', '💲 Heavy Dollar Sign'), ('💳', '💳 Credit Card'), ('💹', '💹 Upwards Trend in Yen'), ('📧', '📧 E-Mail Symbol'), ('📨', '📨 Incoming Envelope'), ('📩', '📩 Going Into Envelope'), ('📤', '📤 Outbox Tray'), ('📥', '📥 Inbox Tray'), ('📦', '📦 Package'), ('📫', '📫 Mailbox'), ('📪', '📪 Closed Mailbox With Lowered Flag'), ('📬', '📬 Open Mailbox With Raised Flag'), ('📭', '📭 Open Mailbox With Lowered Flag'), ('📮', '📮 Postbox'), ('📝', '📝 Memo'), ('💼', '💼 Briefcase'), ('📁', '📁 File Folder'), ('📂', '📂 Open File Folder'), ('📅', '📅 Dated'), ('📆', '📆 Tear-Off Calendar'), ('📇', '📇 Card Index'), ('📈', '📈 Up Trend'), ('📉', '📉 Down Trend'), ('📊', '📊 Bar Chart'), ('📋', '📋 Clipboard'), ('📌', '📌 Pushpin'), ('📍', '📍 Location'), ('📎', '📎 Paperclip'), ('📏', '📏 Straight Line'), ('📐', '📐 Three Sides'), ('📛', '📛 Name Badge'), ('🔒', '🔒 Lock'), ('🔓', '🔓 Open Lock'), ('🔏', '🔏 Lock With Ink Pen'), ('🔐', '🔐 Closed Lock With Key'), ('🔑', '🔑 Key'), ('🔨', '🔨 Hammer'), ('🔧', '🔧 Spanner'), ('🔩', '🔩 Calipers'), ('🔗', '🔗 Link Symbol'), ('💉', '💉 Syringe'), ('💊', '💊 Pill'), ('🔪', '🔪 Chef Knife'), ('🔫', '🔫 Pistol'), ('🚬', '🚬 Durry'), ('🏁', '🏁 Get Set Go'), ('🚩', '🚩 Triangular Flag on Post'), ('🇦🇫', '🇦🇫 Afghanistan'), ('🇦🇽', '🇦🇽 Åland Islands'), ('🇦🇱', '🇦🇱 Albania'), ('🇩🇿', '🇩🇿 Algeria'), ('🇦🇸', '🇦🇸 American Samoa'), ('🇦🇩', '🇦🇩 Andorra'), ('🇦🇴', '🇦🇴 Angola'), ('🇦🇮', '🇦🇮 Anguilla'), ('🇦🇶', '🇦🇶 Antarctica'), ('🇦🇬', '🇦🇬 Antigua & Barbuda'), ('🇦🇷', '🇦🇷 Argentina'), ('🇦🇲', '🇦🇲 Armenia'), ('🇦🇼', '🇦🇼 Aruba'), ('🇦🇨', '🇦🇨 Ascension Island'), ('🇦🇺', '🇦🇺 Australia'), ('🇦🇹', '🇦🇹 Austria'), ('🇦🇿', '🇦🇿 Azerbaijan'), ('🇧🇸', '🇧🇸 Bahamas'), ('🇧🇭', '🇧🇭 Bahrain'), ('🇧🇩', '🇧🇩 Bangladesh'), ('🇧🇧', '🇧🇧 Barbados'), ('🇧🇾', '🇧🇾 Belarus'), ('🇧🇪', '🇧🇪 Belgium'), ('🇧🇿', '🇧🇿 Belize'), ('🇧🇯', '🇧🇯 Benin'), ('🇧🇲', '🇧🇲 Bermuda'), ('🇧🇹', '🇧🇹 Bhutan'), ('🇧🇴', '🇧🇴 Bolivia'), ('🇧🇦', '🇧🇦 Bosnia & Herzegovina'), ('🇧🇼', '🇧🇼 Botswana'), ('🇧🇻', '🇧🇻 Bouvet Island'), ('🇧🇷', '🇧🇷 Brazil'), ('🇮🇴', '🇮🇴 British Indian Ocean Territory'), ('🇻🇬', '🇻🇬 British Virgin Islands'), ('🇧🇳', '🇧🇳 Brunei'), ('🇧🇬', '🇧🇬 Bulgaria'), ('🇧🇫', '🇧🇫 Burkina Faso'), ('🇧🇮', '🇧🇮 Burundi'), ('🇰🇭', '🇰🇭 Cambodia'), ('🇨🇲', '🇨🇲 Cameroon'), ('🇨🇦', '🇨🇦 Canada'), ('🇮🇨', '🇮🇨 Canary Islands'), ('🇨🇻', '🇨🇻 Cape Verde'), ('🇧🇶', '🇧🇶 Caribbean Netherlands'), ('🇰🇾', '🇰🇾 Cayman Islands'), ('🇨🇫', '🇨🇫 Central African Republic'), ('🇪🇦', '🇪🇦 Ceuta & Melilla'), ('🇹🇩', '🇹🇩 Chad'), ('🇨🇱', '🇨🇱 Chile'), ('🇨🇳', '🇨🇳 China'), ('🇨🇽', '🇨🇽 Christmas Island'), ('🇨🇵', '🇨🇵 Clipperton Island'), ('🇨🇨', '🇨🇨 Cocos Islands'), ('🇨🇴', '🇨🇴 Colombia'), ('🇰🇲', '🇰🇲 Comoros'), ('🇨🇬', '🇨🇬 Congo - Brazzaville'), ('🇨🇩', '🇨🇩 Congo - Kinshasa'), ('🇨🇰', '🇨🇰 Cook Islands'), ('🇨🇷', '🇨🇷 Costa Rica'), ('🇨🇮', '🇨🇮 Côte D’Ivoire'), ('🇭🇷', '🇭🇷 Croatia'), ('🇨🇺', '🇨🇺 Cuba'), ('🇨🇼', '🇨🇼 Curaçao'), ('🇨🇾', '🇨🇾 Cyprus'), ('🇨🇿', '🇨🇿 Czech Republic'), ('🇩🇰', '🇩🇰 Denmark'), ('🇩🇬', '🇩🇬 Diego Garcia'), ('🇩🇯', '🇩🇯 Djibouti'), ('🇩🇲', '🇩🇲 Dominica'), ('🇩🇴', '🇩🇴 Dominican Republic'), ('🇪🇨', '🇪🇨 Ecuador'), ('🇪🇬', '🇪🇬 Egypt'), ('🇸🇻', '🇸🇻 El Salvador'), ('🇬🇶', '🇬🇶 Equatorial Guinea'), ('🇪🇷', '🇪🇷 Eritrea'), ('🇪🇪', '🇪🇪 Estonia'), ('🇪🇹', '🇪🇹 Ethiopia'), ('🇪🇺', '🇪🇺 European Union'), ('🇫🇰', '🇫🇰 Falkland Islands'), ('🇫🇴', '🇫🇴 Faroe Islands'), ('🇫🇯', '🇫🇯 Fiji'), ('🇫🇮', '🇫🇮 Finland'), ('🇫🇷', '🇫🇷 France'), ('🇬🇫', '🇬🇫 French Guiana'), ('🇵🇫', '🇵🇫 French Polynesia'), ('🇹🇫', '🇹🇫 French Southern Territories'), ('🇬🇦', '🇬🇦 Gabon'), ('🇬🇲', '🇬🇲 Gambia'), ('🇬🇪', '🇬🇪 Georgia'), ('🇩🇪', '🇩🇪 Germany'), ('🇬🇭', '🇬🇭 Ghana'), ('🇬🇮', '🇬🇮 Gibraltar'), ('🇬🇷', '🇬🇷 Greece'), ('🇬🇱', '🇬🇱 Greenland'), ('🇬🇩', '🇬🇩 Grenada'), ('🇬🇵', '🇬🇵 Guadeloupe'), ('🇬🇺', '🇬🇺 Guam'), ('🇬🇹', '🇬🇹 Guatemala'), ('🇬🇬', '🇬🇬 Guernsey'), ('🇬🇳', '🇬🇳 Guinea'), ('🇬🇼', '🇬🇼 Guinea-Bissau'), ('🇬🇾', '🇬🇾 Guyana'), ('🇭🇹', '🇭🇹 Haiti'), ('🇭🇲', '🇭🇲 Heard & McDonald Islands'), ('🇭🇳', '🇭🇳 Honduras'), ('🇭🇰', '🇭🇰 Hong Kong'), ('🇭🇺', '🇭🇺 Hungary'), ('🇮🇸', '🇮🇸 Iceland'), ('🇮🇳', '🇮🇳 India'), ('🇮🇩', '🇮🇩 Indonesia'), ('🇮🇷', '🇮🇷 Iran'), ('🇮🇶', '🇮🇶 Iraq'), ('🇮🇪', '🇮🇪 Ireland'), ('🇮🇲', '🇮🇲 Isle of Man'), ('🇮🇱', '🇮🇱 Israel'), ('🇮🇹', '🇮🇹 Italy'), ('🇯🇲', '🇯🇲 Jamaica'), ('🇯🇵', '🇯🇵 Japan'), ('🇯🇪', '🇯🇪 Jersey'), ('🇯🇴', '🇯🇴 Jordan'), ('🇰🇿', '🇰🇿 Kazakhstan'), ('🇰🇪', '🇰🇪 Kenya'), ('🇰🇮', '🇰🇮 Kiribati'), ('🇽🇰', '🇽🇰 Kosovo'), ('🇰🇼', '🇰🇼 Kuwait'), ('🇰🇬', '🇰🇬 Kyrgyzstan'), ('🇱🇦', '🇱🇦 Laos'), ('🇱🇻', '🇱🇻 Latvia'), ('🇱🇧', '🇱🇧 Lebanon'), ('🇱🇸', '🇱🇸 Lesotho'), ('🇱🇷', '🇱🇷 Liberia'), ('🇱🇾', '🇱🇾 Libya'), ('🇱🇮', '🇱🇮 Liechtenstein'), ('🇱🇹', '🇱🇹 Lithuania'), ('🇱🇺', '🇱🇺 Luxembourg'), ('🇲🇴', '🇲🇴 Macau'), ('🇲🇰', '🇲🇰 Macedonia'), ('🇲🇬', '🇲🇬 Madagascar'), ('🇲🇼', '🇲🇼 Malawi'), ('🇲🇾', '🇲🇾 Malaysia'), ('🇲🇻', '🇲🇻 Maldives'), ('🇲🇱', '🇲🇱 Mali'), ('🇲🇹', '🇲🇹 Malta'), ('🇲🇭', '🇲🇭 Marshall Islands'), ('🇲🇶', '🇲🇶 Martinique'), ('🇲🇷', '🇲🇷 Mauritania'), ('🇲🇺', '🇲🇺 Mauritius'), ('🇾🇹', '🇾🇹 Mayotte'), ('🇲🇽', '🇲🇽 Mexico'), ('🇫🇲', '🇫🇲 Micronesia'), ('🇲🇩', '🇲🇩 Moldova'), ('🇲🇨', '🇲🇨 Monaco'), ('🇲🇳', '🇲🇳 Mongolia'), ('🇲🇪', '🇲🇪 Montenegro'), ('🇲🇸', '🇲🇸 Montserrat'), ('🇲🇦', '🇲🇦 Morocco'), ('🇲🇿', '🇲🇿 Mozambique'), ('🇲🇲', '🇲🇲 Myanmar'), ('🇳🇦', '🇳🇦 Namibia'), ('🇳🇷', '🇳🇷 Nauru'), ('🇳🇵', '🇳🇵 Nepal'), ('🇳🇱', '🇳🇱 Netherlands'), ('🇳🇨', '🇳🇨 New Caledonia'), ('🇳🇿', '🇳🇿 New Zealand'), ('🇳🇮', '🇳🇮 Nicaragua'), ('🇳🇪', '🇳🇪 Niger'), ('🇳🇬', '🇳🇬 Nigeria'), ('🇳🇺', '🇳🇺 Niue'), ('🇳🇫', '🇳🇫 Norfolk Island'), ('🇲🇵', '🇲🇵 Northern Mariana Islands'), ('🇰🇵', '🇰🇵 North Korea'), ('🇳🇴', '🇳🇴 Norway'), ('🇴🇲', '🇴🇲 Oman'), ('🇵🇰', '🇵🇰 Pakistan'), ('🇵🇼', '🇵🇼 Palau'), ('🇵🇸', '🇵🇸 Palestinian Territories'), ('🇵🇦', '🇵🇦 Panama'), ('🇵🇬', '🇵🇬 Papua New Guinea'), ('🇵🇾', '🇵🇾 Paraguay'), ('🇵🇪', '🇵🇪 Peru'), ('🇵🇭', '🇵🇭 Philippines'), ('🇵🇳', '🇵🇳 Pitcairn Islands'), ('🇵🇱', '🇵🇱 Poland'), ('🇵🇹', '🇵🇹 Portugal'), ('🇵🇷', '🇵🇷 Puerto Rico'), ('🇶🇦', '🇶🇦 Qatar'), ('🇷🇪', '🇷🇪 Réunion'), ('🇷🇴', '🇷🇴 Romania'), ('🇷🇺', '🇷🇺 Russia'), ('🇷🇼', '🇷🇼 Rwanda'), ('🇼🇸', '🇼🇸 Samoa'), ('🇸🇲', '🇸🇲 San Marino'), ('🇸🇹', '🇸🇹 São Tomé & Príncipe'), ('🇸🇦', '🇸🇦 Saudi Arabia'), ('🇸🇳', '🇸🇳 Senegal'), ('🇷🇸', '🇷🇸 Serbia'), ('🇸🇨', '🇸🇨 Seychelles'), ('🇸🇱', '🇸🇱 Sierra Leone'), ('🇸🇬', '🇸🇬 Singapore'), ('🇸🇽', '🇸🇽 Sint Maarten'), ('🇸🇰', '🇸🇰 Slovakia'), ('🇸🇮', '🇸🇮 Slovenia'), ('🇸🇧', '🇸🇧 Solomon Islands'), ('🇸🇴', '🇸🇴 Somalia'), ('🇿🇦', '🇿🇦 South Africa'), ('🇬🇸', '🇬🇸 South Georgia & South Sandwich Islands'), ('🇰🇷', '🇰🇷 South Korea'), ('🇸🇸', '🇸🇸 South Sudan'), ('🇪🇸', '🇪🇸 Spain'), ('🇱🇰', '🇱🇰 Sri Lanka'), ('🇧🇱', '🇧🇱 St. Barthélemy'), ('🇸🇭', '🇸🇭 St. Helena'), ('🇰🇳', '🇰🇳 St. Kitts & Nevis'), ('🇱🇨', '🇱🇨 St. Lucia'), ('🇲🇫', '🇲🇫 St. Martin'), ('🇵🇲', '🇵🇲 St. Pierre & Miquelon'), ('🇻🇨', '🇻🇨 St. Vincent & Grenadines'), ('🇸🇩', '🇸🇩 Sudan'), ('🇸🇷', '🇸🇷 Suriname'), ('🇸🇯', '🇸🇯 Svalbard & Jan Mayen'), ('🇸🇿', '🇸🇿 Swaziland'), ('🇸🇪', '🇸🇪 Sweden'), ('🇨🇭', '🇨🇭 Switzerland'), ('🇸🇾', '🇸🇾 Syria'), ('🇹🇼', '🇹🇼 Taiwan'), ('🇹🇯', '🇹🇯 Tajikistan'), ('🇹🇿', '🇹🇿 Tanzania'), ('🇹🇭', '🇹🇭 Thailand'), ('🇹🇱', '🇹🇱 Timor-Leste'), ('🇹🇬', '🇹🇬 Togo'), ('🇹🇰', '🇹🇰 Tokelau'), ('🇹🇴', '🇹🇴 Tonga'), ('🇹🇹', '🇹🇹 Trinidad & Tobago'), ('🇹🇦', '🇹🇦 Tristan Da Cunha'), ('🇹🇳', '🇹🇳 Tunisia'), ('🇹🇷', '🇹🇷 Turkey'), ('🇹🇲', '🇹🇲 Turkmenistan'), ('🇹🇨', '🇹🇨 Turks & Caicos Islands'), ('🇹🇻', '🇹🇻 Tuvalu'), ('🇺🇬', '🇺🇬 Uganda'), ('🇺🇦', '🇺🇦 Ukraine'), ('🇦🇪', '🇦🇪 United Arab Emirates'), ('🇬🇧', '🇬🇧 United Kingdom'), ('🇺🇸', '🇺🇸 United States'), ('🇺🇾', '🇺🇾 Uruguay'), ('🇺🇲', '🇺🇲 U.S. Outlying Islands'), ('🇻🇮', '🇻🇮 U.S. Virgin Islands'), ('🇺🇿', '🇺🇿 Uzbekistan'), ('🇻🇺', '🇻🇺 Vanuatu'), ('🇻🇦', '🇻🇦 Vatican City'), ('🇻🇪', '🇻🇪 Venezuela'), ('🇻🇳', '🇻🇳 Vietnam'), ('🇼🇫', '🇼🇫 Wallis & Futuna'), ('🇪🇭', '🇪🇭 Western Sahara'), ('🇾🇪', '🇾🇪 Yemen'), ('🇿🇲', '🇿🇲 Zambia'), ('🇿🇼', '🇿🇼 Zimbabwe'), ('🔃', '🔃 Clockwise Arrows'), ('🔄', '🔄 Anticlockwise Arrows'), ('🔙', '🔙 Back'), ('🔚', '🔚 End'), ('🔛', '🔛 On'), ('🔜', '🔜 Soon'), ('🔝', '🔝 Top'), ('🔰', '🔰 Beginner'), ('🔮', '🔮 Crystal Ball'), ('🔯', '🔯 Six Pointed Star With Middle Dot'), ('✅', '✅ White Heavy Check Mark'), ('❌', '❌ Cross'), ('❎', '❎ Negative Squared Cross Mark'), ('➕', '➕ Heavy Plus Sign'), ('➖', '➖ Heavy Minus Sign'), ('➗', '➗ Heavy Division Sign'), ('➰', '➰ Curly Loop'), ('➿', '➿ Double Curly Loop'), ('❓', '❓ Question'), ('❔', '❔ White Question Mark Ornament'), ('❕', '❕ White Exclamation Mark Ornament'), ('💯', '💯 Hundred Points'), ('🔞', '🔞 Over Eighteen'), ('🔠', '🔠 Latin Capital Letters'), ('🔡', '🔡 Latin Small Letters'), ('🔢', '🔢 Numbers'), ('🔣', '🔣 Symbols'), ('🔤', '🔤 Latin Letters'), ('🅰️', '🅰️ Squared A'), ('🆎', '🆎 Squared AB'), ('🅱️', '🅱️ Squared B'), ('🆑', '🆑 Squared CL'), ('🆒', '🆒 Cool Square'), ('🆓', '🆓 Squared Free'), ('🆔', '🆔 Squared ID'), ('🆕', '🆕 New Square'), ('🆖', '🆖 Squared NG'), ('🅾️', '🅾️ Squared O'), ('🆗', '🆗 OK Square'), ('🆘', '🆘 SOS Square'), ('🆙', '🆙 Squared Up!'), ('🆚', '🆚 Squared Vs'), ('🈁', '🈁 Squared Katakana Koko'), ('🈂️', '🈂️ Squared Katakana Sa'), ('🈷️', '🈷️ Squared 月 (Moon)'), ('🈶', '🈶 Squared 有 (Have)'), ('🉐', '🉐 Circled Ideograph Advantage'), ('🈹', '🈹 Squared CJK Unified Ideograph-5272'), ('🈲', '🈲 Squared CJK Unified Ideograph-7981'), ('🉑', '🉑 Circled 可 (Accept)'), ('🈸', '🈸 Squared CJK Unified Ideograph-7533'), ('🈴', '🈴 Squared CJK Unified Ideograph-5408'), ('🈳', '🈳 Squared CJK Unified Ideograph-7a7a'), ('🈺', '🈺 Squared CJK Unified Ideograph-55b6'), ('🈵', '🈵 Squared CJK Unified Ideograph-6e80'), ('🔶', '🔶 Large Orange Diamond'), ('🔷', '🔷 Large Blue Diamond'), ('🔸', '🔸 Small Orange Diamond'), ('🔹', '🔹 Small Blue Diamond'), ('🔺', '🔺 Up-Pointing Red Triangle'), ('🔻', '🔻 Down-Pointing Red Triangle'), ('💠', '💠 Diamond Shape With a Dot Inside'), ('🔘', '🔘 Radio Button'), ('🔲', '🔲 Black Square Button'), ('🔳', '🔳 White Square Button'), ('🔴', '🔴 Large Red Circle'), ('🔵', '🔵 Large Blue Circle'), ('😀', '😀 Grinning'), ('😗', '😗 Kissing'), ('😙', '😙 Smooch'), ('😑', '😑 True Neutral'), ('😮', '😮 Stunned'), ('😯', '😯 Hushed'), ('😴', '😴 Sleepy'), ('😛', '😛 Tongue'), ('😕', '😕 Confused'), ('😟', '😟 Worried'), ('😦', '😦 Frowning Face With Open Mouth'), ('😧', '😧 Anguish Face'), ('😬', '😬 Grimace'), ('🙂', '🙂 Slightly Smiling'), ('🙁', '🙁 Slightly Frowning'), ('🕵', '🕵 Spy'), ('🗣', '🗣 Speaking Head in Silhouette'), ('🕴', '🕴 Man in Business Suit Levitating'), ('🖕', '🖕 Middle Finger'), ('🖖', '🖖 Vulcan Hand'), ('🖐', '🖐 Raised Hand With Fingers Splayed'), ('👁', '👁 Eye'), ('🕳', '🕳 Hole'), ('🗯', '🗯 Right Anger Bubble'), ('🕶', '🕶 Sunglasses'), ('🛍', '🛍 Shopping'), ('🐿', '🐿 Chipmunk'), ('🕊', '🕊 Peace Dove'), ('🕷', '🕷 Spider'), ('🕸', '🕸 Spider Web'), ('🏵', '🏵 Rosette'), ('🌶', '🌶 Chilli'), ('🍽', '🍽 Fork and Knife With Plate'), ('🗺', '🗺 World Map'), ('🏔', '🏔 Snow Capped Mountain'), ('🏕', '🏕 Camping'), ('🏖', '🏖 Beach'), ('🏜', '🏜 Desert'), ('🏝', '🏝 Desert Island'), ('🏞', '🏞 National Park'), ('🏟', '🏟 Stadium'), ('🏛', '🏛 Architecture'), ('🏗', '🏗 Building Construction'), ('🏘', '🏘 House Buildings'), ('🏙', '🏙 Cityscape'), ('🏚', '🏚 Derelict House Building'), ('🖼', '🖼 Frame With Picture'), ('🛢', '🛢 Oil Drum'), ('🛣', '🛣 Motorway'), ('🛤', '🛤 Railway Track'), ('🛳', '🛳 Passenger Ship'), ('🛥', '🛥 Boat'), ('🛩', '🛩 Airplane'), ('🛫', '🛫 Airplane Departure'), ('🛬', '🛬 Airplane Arriving'), ('🛰', '🛰 Satellite'), ('🛎', '🛎 Service Bell'), ('🛌', '🛌 Bed'), ('🛏', '🛏 Bed'), ('🛋', '🛋 Couch and Lamp'), ('🕰', '🕰 Mantelpiece'), ('🌡', '🌡 Thermometer'), ('🌤', '🌤 Small Cloud'), ('🌥', '🌥 White Sun Behind Cloud'), ('🌦', '🌦 White Sun Behind Cloud With Rain'), ('🌧', '🌧 Cloud With Rain'), ('🌨', '🌨 Cloud With Snow'), ('🌩', '🌩 Lightning'), ('🌪', '🌪 Tornado'), ('🌫', '🌫 Fog'), ('🌬', '🌬 Blowing'), ('🎖', '🎖 Medal'), ('🎗', '🎗 Ribbon'), ('🎞', '🎞 Film'), ('🎟', '🎟 Admission Tickets'), ('🏷', '🏷 Label'), ('🏌', '🏌 Golfer'), ('🏋', '🏋 Lifting'), ('🏎', '🏎 Racing Car'), ('🏍', '🏍 Racing Motorcycle'), ('🏅', '🏅 Medal'), ('🕹', '🕹 Joystick'), ('⏸', '⏸ Double Vertical Bar'), ('⏹', '⏹ Black Square for Stop'), ('⏺', '⏺ Black Circle for Record'), ('🎙', '🎙 Microphone'), ('🎚', '🎚 Level Slider'), ('🎛', '🎛 Control Knobs'), ('🖥', '🖥 Desktop'), ('🖨', '🖨 Printer'), ('🖱', '🖱 Three Button Mouse'), ('🖲', '🖲 Trackball'), ('📽', '📽 Film Projector'), ('📸', '📸 Camera With Flash'), ('🕯', '🕯 Candle'), ('🗞', '🗞 Newspaper'), ('🗳', '🗳 Ballot Box With Ballot'), ('🖋', '🖋 Fancy Pen'), ('🖊', '🖊 Lower Left Ballpoint Pen'), ('🖌', '🖌 Lower Left Paintbrush'), ('🖍', '🖍 Lower Left Crayon'), ('🗂', '🗂 Card Index Dividers'), ('🗒', '🗒 Spiral Note Pad'), ('🗓', '🗓 Spiral Calendar Pad'), ('🖇', '🖇 Linked Paperclips'), ('🗃', '🗃 Card File Box'), ('🗄', '🗄 File Cabinet'), ('🗑', '🗑 Wastebasket'), ('🗝', '🗝 Old Key'), ('🛠', '🛠 Tools'), ('🗜', '🗜 Compression'), ('🗡', '🗡 Dagger'), ('🛡', '🛡 Shield'), ('🏳', '🏳 White Flag'), ('🏴', '🏴 Black Flag'), ('🕉', '🕉 Om Symbol'), ('🗨', '🗨 Left Speech Bubble'), ('🤗', '🤗 Hugging'), ('🤔', '🤔 Thinking'), ('🙄', '🙄 Rolling Eyes'), ('🤐', '🤐 Hushed'), ('🤓', '🤓 Nerd'), ('🙃', '🙃 Upside Down'), ('🤒', '🤒 Sick'), ('🤕', '🤕 Hurt Head'), ('🤑', '🤑 Money'), ('🏻', '🏻 Emoji Modifier 1-2'), ('🏼', '🏼 Emoji Modifier 3'), ('🏽', '🏽 Emoji Modifier 4'), ('🏾', '🏾 Emoji Modifier 5'), ('🏿', '🏿 Emoji Modifier 6'), ('🤘', '🤘 Rock On'), ('📿', '📿 Prayer Beads'), ('🤖', '🤖 Robot'), ('🦁', '🦁 Lion'), ('🦄', '🦄 Unicorn'), ('🦃', '🦃 Turkey'), ('🦀', '🦀 Crab'), ('🦂', '🦂 Scorpion'), ('🧀', '🧀 Cheese'), ('🌭', '🌭 Hot Dog'), ('🌮', '🌮 Taco'), ('🌯', '🌯 Burrito'), ('🍿', '🍿 Popcorn'), ('🍾', '🍾 Popping Cork'), ('🏺', '🏺 Amphora'), ('🛐', '🛐 Place of Worship'), ('🕋', '🕋 Kaaba'), ('🕌', '🕌 Mosque'), ('🕍', '🕍 Synagogue'), ('🕎', '🕎 Menorah'), ('🏏', '🏏 Bat and Ball'), ('🏐', '🏐 Volleyball'), ('🏑', '🏑 Field Hockey'), ('🏒', '🏒 Ice Hockey'), ('🏓', '🏓 Table Tennis'), ('🏸', '🏸 Badminton'), ('🏹', '🏹 Archer'), ('🤣', '🤣 ROFL Face'), ('🤤', '🤤 Drooling'), ('🤢', '🤢 Nauseated'), ('🤧', '🤧 Sneezing'), ('🤠', '🤠 Cowboy'), ('🤡', '🤡 Clown'), ('🤥', '🤥 Lying'), ('🤴', '🤴 Prince'), ('🤵', '🤵 Tuxedo Man'), ('🤰', '🤰 Pregnant'), ('🤶', '🤶 Mrs. Claus'), ('🤦', '🤦 Facepalm'), ('🤷', '🤷 Shrugging'), ('🕺', '🕺 Man Dancing'), ('🤺', '🤺 Fencing'), ('🤸', '🤸 Cartwheel'), ('🤼', '🤼 Wrestling'), ('🤽', '🤽 Water Polo'), ('🤾', '🤾 Handball'), ('🤹', '🤹 Juggling'), ('🤳', '🤳 Selfie'), ('🤞', '🤞 Luck Hand'), ('🤙', '🤙 Call Me Hand'), ('🤛', '🤛 Left-Facing Fist'), ('🤜', '🤜 Right-Facing Fist'), ('🤚', '🤚 Raised Back of Hand'), ('🤝', '🤝 Business Hi'), ('🖤', '🖤 Black Heart'), ('🦍', '🦍 Gorilla'), ('🦊', '🦊 Fox'), ('🦌', '🦌 Deer'), ('🦏', '🦏 Rhinoceros'), ('🦇', '🦇 Bat'), ('🦅', '🦅 Eagle'), ('🦆', '🦆 Duck'), ('🦉', '🦉 Owl'), ('🦎', '🦎 Lizard'), ('🦈', '🦈 Shark'), ('🦐', '🦐 Shrimp'), ('🦑', '🦑 Squid'), ('🦋', '🦋 Butterfly'), ('🥀', '🥀 Wilted'), ('🥝', '🥝 Kiwifruit'), ('🥑', '🥑 Pricey Fruit'), ('🥔', '🥔 Potato'), ('🥕', '🥕 Carrot'), ('🥒', '🥒 Cucumber'), ('🥜', '🥜 Peanuts'), ('🥐', '🥐 Croissant'), ('🥖', '🥖 Bread Sword'), ('🥞', '🥞 Pancakes'), ('🥓', '🥓 Bacon'), ('🥙', '🥙 Stuffed Flatbread'), ('🥚', '🥚 Chicken Rock'), ('🥘', '🥘 Shallow Pan'), ('🥗', '🥗 Salad'), ('🥛', '🥛 Cow Juice'), ('🥂', '🥂 Clinking Glasses'), ('🥃', '🥃 Tumbler'), ('🥄', '🥄 Spoon'), ('🛴', '🛴 Scoot Scoot'), ('🛵', '🛵 Motor Scooter'), ('🛑', '🛑 Stop Sign'), ('🛶', '🛶 Canoe'), ('🥇', '🥇 Gold Medal'), ('🥈', '🥈 Silver Medal'), ('🥉', '🥉 Participation'), ('🥊', '🥊 Boxing'), ('🥋', '🥋 Martial Arts'), ('🥅', '🥅 Hashtag Goals'), ('🥁', '🥁 Drum Roll'), ('🛒', '🛒 Food Ute'), ('🤩', '🤩 Star Struck'), ('🤨', '🤨 Unexpected Face'), ('🤯', '🤯 Mind Blown'), ('🤪', '🤪 Zany Face'), ('🤬', '🤬 Swear Face'), ('🤮', '🤮 Vomiting'), ('🤫', '🤫 Shushing'), ('🤭', '🤭 Hand Over Mouth'), ('🧐', '🧐 Monocle'), ('🧒', '🧒 Child Face'), ('🧑', '🧑 Adult'), ('🧓', '🧓 Older Adult'), ('🧕', '🧕 Headscarf'), ('🧔', '🧔 Bearded Person'), ('🤱', '🤱 Breast Feeding'), ('🧙', '🧙 Mage'), ('🧚', '🧚 Fairy'), ('🧛', '🧛 Vampire'), ('🧜', '🧜 Merperson'), ('🧝', '🧝 Cosplay'), ('🧞', '🧞 Genie'), ('🧟', '🧟 Unalive'), ('🧖', '🧖 Steamy Room'), ('🧗', '🧗 Person Climbing'), ('🧘', '🧘 Lotus Position'), ('🤟', '🤟 Love-You Gesture'), ('🤲', '🤲 Palms Up Together'), ('🧠', '🧠 Big Brain'), ('🧡', '🧡 Orange Heart'), ('🧣', '🧣 Neck Hider'), ('🧤', '🧤 Hand Socks'), ('🧥', '🧥 Coat'), ('🧦', '🧦 Feet Gloves'), ('🧢', '🧢 Billed Cap'), ('🦓', '🦓 Zebra'), ('🦒', '🦒 Giraffe'), ('🦔', '🦔 Spikehog'), ('🦕', '🦕 Long Neck'), ('🦖', '🦖 Big Roar'), ('🦗', '🦗 Cricket'), ('🥥', '🥥 Coconut'), ('🥦', '🥦 Tiny Tree'), ('🥨', '🥨 Twisty Bread'), ('🥩', '🥩 Cut of Meat'), ('🥪', '🥪 Sandwich'), ('🥣', '🥣 Bowl With Spoon'), ('🥫', '🥫 Canned Good'), ('🥟', '🥟 Dumpling'), ('🥠', '🥠 Tasty Future'), ('🥡', '🥡 Takeout Box'), ('🥧', '🥧 Pie'), ('🥤', '🥤 Cup With Straw'), ('🥢', '🥢 Chopsticks'), ('🛸', '🛸 Alien Plane'), ('🛷', '🛷 Sled'), ('🥌', '🥌 Curling'), ('🥰', '🥰 Smiling Face With 3 Hearts'), ('🥵', '🥵 Overheated'), ('🥶', '🥶 Freezing Face'), ('🥴', '🥴 Woozy Face'), ('🥳', '🥳 Party Face'), ('🥺', '🥺 Pleading Face'), ('🦵', '🦵 Leg'), ('🦶', '🦶 Foot'), ('🦷', '🦷 Tooth'), ('🦴', '🦴 Bone'), ('🦸', '🦸 Superhero'), ('🦹', '🦹 Supervillain'), ('🦝', '🦝 Trash Bandit'), ('🦙', '🦙 Llama'), ('🦛', '🦛 Hippopotamus'), ('🦘', '🦘 Kangaroo'), ('🦡', '🦡 Badger'), ('🦢', '🦢 Swan'), ('🦚', '🦚 Peacock'), ('🦜', '🦜 Parrot'), ('🦟', '🦟 Mosquito'), ('🦠', '🦠 Microbe'), ('🥭', '🥭 Mango'), ('🥬', '🥬 Leafy Green'), ('🥯', '🥯 Bagel'), ('🧂', '🧂 Salty'), ('🥮', '🥮 Moon Cake'), ('🦞', '🦞 Lobster'), ('🧁', '🧁 Cupcake'), ('🧭', '🧭 Compass'), ('🧱', '🧱 Brick'), ('🛹', '🛹 Skateboard'), ('🧳', '🧳 Baggage'), ('🧨', '🧨 Firework'), ('🧧', '🧧 Red Envelope'), ('🥎', '🥎 Softball'), ('🥏', '🥏 Throwing Disc'), ('🥍', '🥍 Lacrosse'), ('🧿', '🧿 Nazar Amulet'), ('🧩', '🧩 Puzzle Piece'), ('🧸', '🧸 Teddy Bear'), ('🧵', '🧵 Thread'), ('🧶', '🧶 Yarn Ball'), ('🥽', '🥽 The Goggles'), ('🥼', '🥼 Lab Coat'), ('🥾', '🥾 Hiking Boot'), ('🥿', '🥿 Flat Shoe'), ('🧮', '🧮 Abacus'), ('🧾', '🧾 Receipt'), ('🧰', '🧰 Toolbox'), ('🧲', '🧲 Magnet'), ('🧪', '🧪 Test Tube'), ('🧫', '🧫 Petri Dish'), ('🧬', '🧬 DNA'), ('🧴', '🧴 Lotion'), ('🧷', '🧷 Safety Pin'), ('🧹', '🧹 Broom'), ('🧺', '🧺 Basket'), ('🧻', '🧻 Roll of Paper'), ('🧼', '🧼 Soap'), ('🧽', '🧽 Fun sponge'), ('🧯', '🧯 Anti-fire Can'), ('🥱', '🥱 Yawning Face'), ('🤎', '🤎 Brown Heart'), ('🤍', '🤍 White Heart'), ('🤏', '🤏 Pinching Hand'), ('🦾', '🦾 Mechanical Arm'), ('🦿', '🦿 Mechanical Leg'), ('🦻', '🦻 Ear with Hearing Aid'), ('🧏', '🧏 Deaf Person'), ('🧍', '🧍 Person Standing'), ('🧎', '🧎 Person Kneeling'), ('🦧', '🦧 Orangutan'), ('🦮', '🦮 Guide Dog'), ('🦥', '🦥 Lazy Tree Dog'), ('🦦', '🦦 Water Dog'), ('🦨', '🦨 Stinky dog'), ('🦩', '🦩 Pink Dog'), ('🧄', '🧄 Garlic'), ('🧅', '🧅 Onion'), ('🧇', '🧇 Waffle'), ('🧆', '🧆 Falafel'), ('🧈', '🧈 Butter'), ('🦪', '🦪 Oyster'), ('🧃', '🧃 Beverage Box'), ('🧉', '🧉 Mate'), ('🧊', '🧊 Cold Cuboid'), ('🛕', '🛕 Hindu Temple'), ('🦽', '🦽 Manual Wheelchair'), ('🦼', '🦼 Motorized Wheelchair'), ('🛺', '🛺 Auto Rickshaw'), ('🪂', '🪂 Parachute'), ('🪐', '🪐 Ringed Planet'), ('🤿', '🤿 Diving Mask'), ('🪀', '🪀 Yo-Yo'), ('🪁', '🪁 Kite'), ('🦺', '🦺 Safety Vest'), ('🥻', '🥻 Sari'), ('🩱', '🩱 One-Piece Swimsuit'), ('🩲', '🩲 Briefs'), ('🩳', '🩳 Shorts'), ('🩰', '🩰 Ballet Shoes'), ('🪕', '🪕 Banjo'), ('🪔', '🪔 Diya Lamp'), ('🪓', '🪓 Axe'), ('🦯', '🦯 White Cane'), ('🩸', '🩸 Drop of Blood'), ('🩹', '🩹 Adhesive Bandage'), ('🩺', '🩺 Stethoscope'), ('🪑', '🪑 Chair'), ('🪒', '🪒 Razor'), ('🟠', '🟠 Orange Circle'), ('🟡', '🟡 Yellow Circle'), ('🟢', '🟢 Green Circle'), ('🟣', '🟣 Purple Circle'), ('🟤', '🟤 Brown Circle'), ('🟥', '🟥 Red Square'), ('🟧', '🟧 Orange Square'), ('🟨', '🟨 Yellow Square'), ('🟩', '🟩 Green Square'), ('🟦', '🟦 Blue Square'), ('🟪', '🟪 Purple Square'), ('🟫', '🟫 Brown Square'), ('🥲', '🥲 Smiling Face with Tear'), ('🥸', '🥸 Disguised Face'), ('🤌', '🤌 Pinched Fingers'), ('🫀', '🫀 Anatomical Heart'), ('🫁', '🫁 Lungs'), ('🥷', '🥷 Ninja'), ('🫂', '🫂 People Hugging'), ('🦬', '🦬 Bison'), ('🦣', '🦣 Mammoth'), ('🦫', '🦫 Beaver'), ('🦤', '🦤 Dodo'), ('🪶', '🪶 Feather'), ('🦭', '🦭 Seal'), ('🪲', '🪲 Beetle'), ('🪳', '🪳 Cockroach'), ('🪰', '🪰 Fly'), ('🪱', '🪱 Worm'), ('🪴', '🪴 Potted Plant'), ('🫐', '🫐 Blueberries'), ('🫒', '🫒 Olive'), ('🫑', '🫑 Bell Pepper'), ('🫓', '🫓 Flatbread'), ('🫔', '🫔 Tamale'), ('🫕', '🫕 Fondue'), ('🫖', '🫖 Teapot'), ('🧋', '🧋 Bubble Tea'), ('🪨', '🪨 Rock'), ('🪵', '🪵 Wood'), ('🛖', '🛖 Hut'), ('🛻', '🛻 Pickup Truck'), ('🛼', '🛼 Roller Skate'), ('🪄', '🪄 Magic Wand'), ('🪅', '🪅 Piñata'), ('🪆', '🪆 Nesting Dolls'), ('🪡', '🪡 Sewing Needle'), ('🪢', '🪢 Knot'), ('🩴', '🩴 Thong Sandal'), ('🪖', '🪖 Military Helmet'), ('🪗', '🪗 Accordion'), ('🪘', '🪘 Long Drum'), ('🪙', '🪙 Coin'), ('🪃', '🪃 Boomerang'), ('🪚', '🪚 Carpentry Saw'), ('🪛', '🪛 Screwdriver'), ('🪝', '🪝 Hook'), ('🪜', '🪜 Ladder'), ('🛗', '🛗 Elevator'), ('🪞', '🪞 Mirror'), ('🪟', '🪟 Window'), ('🪠', '🪠 Plunger'), ('🪤', '🪤 Mouse Trap'), ('🪣', '🪣 Bucket'), ('🪥', '🪥 Toothbrush'), ('🪦', '🪦 Headstone'), ('🪧', '🪧 Placard')], default=None, max_length=3, null=True, verbose_name='emoji'),
        ),
    ]
